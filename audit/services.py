from .models import AuditLog


def log_event(user, action, object_id=None, metadata=None):
    AuditLog.objects.create(
        user=user,
        action=action,
        object_id=object_id,
        org_id=getattr(user, "org_id", None),
        metadata=metadata or {}
    )
