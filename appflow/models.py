from django.db import models

class Project(models.Model):
    """Model to store the project details."""
    project = models.CharField(null=False, blank=False, max_length=100)
    created_on = models.DateTimeField(auto_now=True)
    files = models.FileField(blank=True, null=True)

    def __str__(self):
        return f"{self.project} created on {self.created_on}"
