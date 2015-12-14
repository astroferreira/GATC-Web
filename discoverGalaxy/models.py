from django.db import models

# Create your models here.
class Galaxy(models.Model):
		galId = models.CharField(max_length=7)
		name = models.CharField(max_length=10)
		colorImgUrl = models.CharField(max_length=200)