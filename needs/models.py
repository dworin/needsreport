from django.db import models

# Create your models here.

class Category(models.Model):
	label = models.CharField(max_length=100)



class Need(models.Model):
	source = models.CharField(max_length=40)
	pub_date = models.DateTimeField('date published')
	sourcetype = models.CharField(max_length=40)
	needtext = models.CharField(max_length=160)
	category = models.ForeignKey(Category)
	locationnote = models.CharField(max_length=100)
	countrycode = models.CharField(max_length=2)
	latitude = models.FloatField()
	longitude = models.FloatField()




