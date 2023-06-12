from django.db import models

class Issue(models.Model):
    subject = models.CharField(max_length=100)
    description = models.TextField()
    submit_date = models.DateTimeField(auto_now_add=True)
    duration = models.PositiveIntegerField()
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.subject
