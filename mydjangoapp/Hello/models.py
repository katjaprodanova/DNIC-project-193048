from django.db import models

# Create your models here.
class Product(models.Model):
	title = models.CharField(max_length=50)	
	description = models.TextField(null=True, blank=True)
	image = models.ImageField(upload_to="images/", null=True, blank=True)
