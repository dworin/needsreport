from django.db import models

# Create your models here.

class Category(models.Model):
	label = models.CharField(max_length=100)

	def __unicode__(self):
		return self.label



class Need(models.Model):
	pub_date = models.DateTimeField('date published', auto_now_add=True)
	SOURCE_CHOICES = (
		('SMS', 'SMS (Twilio)'),
		('WEB', 'Needs Report Website'),
		)
	sourcetype = models.CharField(max_length=3, choices=SOURCE_CHOICES)
	source = models.CharField(max_length=40)
	needtext = models.CharField(max_length=160)
	category = models.ForeignKey(Category)
	locationnote = models.CharField(max_length=100)
	countrycode = models.CharField(max_length=2)
	latitude = models.FloatField()
	longitude = models.FloatField()

	def __unicode__(self):
		return self.source + ': ' + self.needtext




