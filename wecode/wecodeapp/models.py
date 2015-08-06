from django.db import models
from django.utils import timezone


class PostUser(models.Model):
    name = models.CharField(max_length=200)
    question1 = models.TextField()
    question2 = models.TextField()
    question3 = models.TextField()
    question4 = models.TextField()
    contactinfo = models.TextField()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name