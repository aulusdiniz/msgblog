from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date=timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Msg(models.Model):
    author = models.ForeignKey('auth.User')
    to = models.CharField(max_length=200)
    text = models.CharField(max_length=2000)
    time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return 'from: ' + self.author+ ' to: '+ self.to

    def send(self):
        self.time = timezone.now()
        self.save()
