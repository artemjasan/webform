from django.db import models

from .ico_validation import ico_exists


class Form(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, blank=True)
    ico = models.CharField(max_length=8, unique=True, validators=[ico_exists])

    def __str__(self):
        return self.name
