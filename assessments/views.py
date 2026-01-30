from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Assessment
from .serializers import AssessmentSerializer


class AssessmentViewSet(ModelViewSet):

    serializer_class = AssessmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Assessment.objects.filter(org=self.request.user.org)

    def perform_create(self, serializer):
        serializer.save(
            org=self.request.user.org,
            created_by=self.request.user
        )
