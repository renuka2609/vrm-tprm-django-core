from django.db import models
from django.conf import settings
from assessments.models import Assessment

class Review(models.Model):
    DECISION_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    org_id = models.IntegerField()
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE)
    reviewer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    comments = models.TextField()
    decision = models.CharField(max_length=20, choices=DECISION_CHOICES, default='pending')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review {self.id}"
