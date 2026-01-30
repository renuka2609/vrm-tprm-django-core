from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response as DRFResponse
from django.utils import timezone

from .models import Response
from .serializers import ResponseSerializer


class ResponseViewSet(ModelViewSet):
    queryset = Response.objects.all()
    serializer_class = ResponseSerializer

    # Save draft = normal create/update already works

    @action(detail=True, methods=["post"])
    def submit(self, request, pk=None):
        obj = self.get_object()

        if obj.is_submitted:
            return DRFResponse(
                {"error": "Already submitted"},
                status=409
            )

        obj.is_submitted = True
        obj.submitted_at = timezone.now()
        obj.save()

        return DRFResponse({"message": "Submitted successfully"})
