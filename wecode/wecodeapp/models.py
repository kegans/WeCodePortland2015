from django.db import models
from django.utils import timezone


class PostUser(models.Model):
    name = models.CharField(max_length=200)
    question1 = models.TextField()
    question2 = models.TextField()
    question3 = models.TextField()
    question4 = models.TextField()
    pic = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')
    created_date = models.DateTimeField(
            default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title