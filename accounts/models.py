from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid

class User(AbstractUser):
    ROLE_CHOICES = (
        ("ADMIN", "Admin"),
        ("REVIEWER", "Reviewer"),
        ("REQUESTER", "Requester"),
        ("VENDOR", "Vendor"),
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default="ADMIN"
    )
    org_id = models.UUIDField(default=uuid.uuid4)
