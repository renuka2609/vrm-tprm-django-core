from django.db import models
from orgs.models import Organization

class Template(models.Model):
    name = models.CharField(max_length=200)
    org = models.ForeignKey("orgs.Organization", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
class TemplateVersion(models.Model):
    template = models.ForeignKey(Template, on_delete=models.CASCADE)
    version = models.IntegerField()
    is_locked = models.BooleanField(default=False)
class Section(models.Model):
    version = models.ForeignKey(TemplateVersion, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
class Question(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    text = models.TextField()
