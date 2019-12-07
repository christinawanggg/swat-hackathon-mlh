from django.db import models

# Create your models here.
class Home(models.Model):
    symptom = models.CharField(max_length=100)
