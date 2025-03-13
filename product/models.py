from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"


class Book(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    is_draft = models.BooleanField(default=True)
    auther = models.ForeignKey(to=User , on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200)

    def __str__(self):
        return f"{self.title} {self.date_created}"
