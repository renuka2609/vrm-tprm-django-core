from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Review
from .serializers import ReviewSerializer

from audit.services import log_event
from services.scoring_client import trigger_scoring


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.filter(org_id=self.request.user.org_id)

    def perform_create(self, serializer):
        review = serializer.save(
            reviewer=self.request.user,
            org_id=self.request.user.org_id
        )

        log_event(
            user=self.request.user,
            action="review_created",
            obj=review
        )

    @action(detail=True, methods=['post'])
    def decision(self, request, pk=None):
        review = self.get_object()
        decision = request.data.get("decision")

        if decision not in ["approved", "rejected"]:
            return Response({"error": "invalid"}, status=400)

        if review.decision != "pending":
            return Response({"error": "already decided"}, status=409)

        review.decision = decision
        review.save()

        if decision == "approved":
            trigger_scoring(review.assessment.id)

        log_event(
            user=request.user,
            action=f"review_{decision}",
            obj=review
        )

        return Response({"status": decision})
