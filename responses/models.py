from django.db import models

class Response(models.Model):
    org_id = models.IntegerField()
    assessment_id = models.IntegerField()
    question_id = models.IntegerField()
    answer = models.TextField()
    is_submitted = models.BooleanField(default=False)
    submitted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Response {self.id}"
