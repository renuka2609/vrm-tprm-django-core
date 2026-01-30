from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Assessment(models.Model):

    STATUS_CHOICES = [
        ("assigned", "Assigned"),
        ("in_progress", "In Progress"),
        ("submitted", "Submitted"),
        ("reviewed", "Reviewed"),
    ]

    org = models.ForeignKey("orgs.Organization", on_delete=models.CASCADE)
    vendor = models.ForeignKey("vendors.Vendor", on_delete=models.CASCADE)

    template_version_id = models.IntegerField()

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="assigned")

    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Assessment {self.id}"
