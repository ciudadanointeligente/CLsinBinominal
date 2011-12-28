from django.db import models

# Create your models here.
class Circunscripcion(models.Model):
	district = models.ForeignKey('District')
	name = models.CharField(max_length = 200)

class District(models.Model):
	name = models.CharField(max_length = 200)

class Comuna(models.Model):
	region = models.ForeignKey('Region')
	district = models.ForeignKey('District')
	name = models.CharField(max_length = 200)

class Region(models.Model):
	name = models.CharField(max_length = 200)
	