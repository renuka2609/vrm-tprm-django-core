from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied

from .models import Template, TemplateVersion
from .serializers import TemplateSerializer, TemplateVersionSerializer
from audit.services import log_event


class TemplateViewSet(ModelViewSet):
    serializer_class = TemplateSerializer
    permission_classes = [IsAuthenticated]
    queryset = Template.objects.all()

    # ✅ ORG SCOPED
    def get_queryset(self):
        user = self.request.user
        if not user.is_authenticated or not hasattr(user, "org"):
            return Template.objects.none()

        return Template.objects.filter(org=user.org)

    # ✅ CREATE TEMPLATE
    def perform_create(self, serializer):
        user = self.request.user

        if getattr(user, "role", None) not in ["ADMIN", "REQUESTER"]:
            raise PermissionDenied("Not allowed to create templates")

        obj = serializer.save(org=user.org)

        log_event(user, "template_created", obj.id)

    # ✅ UPDATE TEMPLATE
    def perform_update(self, serializer):
        obj = serializer.save()
        log_event(self.request.user, "template_updated", obj.id)

    # ✅ CREATE NEW VERSION
    @action(detail=True, methods=["post"])
    def create_version(self, request, pk=None):
        template = self.get_object()

        # next version number
        next_version = template.versions.count() + 1

        version = TemplateVersion.objects.create(
            template=template,
            version_number=next_version,
            created_by=request.user
        )

        log_event(request.user, "template_version_created", version.id)

        return Response({
            "template_id": template.id,
            "version": next_version
        })

    # ✅ LIST VERSIONS
    @action(detail=True, methods=["get"])
    def versions(self, request, pk=None):
        template = self.get_object()
        qs = template.versions.all()

        data = TemplateVersionSerializer(qs, many=True).data
        return Response(data)

    # ✅ VERSION DETAIL (LOCKED VIEW)
    @action(detail=True, methods=["get"], url_path="versions/(?P<version_id>[^/.]+)")
    def version_detail(self, request, pk=None, version_id=None):
        template = self.get_object()

        try:
            version = template.versions.get(id=version_id)
        except TemplateVersion.DoesNotExist:
            return Response({"error": "Version not found"}, status=404)

        data = TemplateVersionSerializer(version).data
        return Response(data)
