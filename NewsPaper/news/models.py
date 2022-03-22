from django.db import models


class News(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
    )
    description = models.TextField()

    data = models.DateTimeField()


    def __str__(self):
        return f'{self.name.title()}: {self.description[:20]}'



class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f'{self.name.title()}'


def dataCreation():
    return None