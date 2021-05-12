from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title
