from django.db import models


# Create your models here.

class Choice(models.Model):
    name = models.CharField(max_length=10,
                            help_text='Enter a description')

    number = models.IntegerField()
