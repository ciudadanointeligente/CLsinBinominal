from django.db import models
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from candidate.models import Candidate
from electoralarea.models import ElectionZone
from electoralarea.models import District
import datetime

# Create your models here.
class ElectionType(models.Model):
	description = models.CharField(max_length = 200)
	def __unicode__(self):
		return self.description

class ElectionSystem(models.Model):
	description = models.CharField(max_length = 100)
	def __unicode__(self):
		return self.description

class Election(models.Model):
	electiontype = models.ForeignKey('ElectionType')
	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = generic.GenericForeignKey('content_type', 'object_id')
	name = models.CharField(max_length = 200)
	date = models.DateField()
	candidates = models.ManyToManyField('candidate.Candidate', through = 'ElectionResult')
	def __unicode__(self):
		return self.name

class ElectionResult(models.Model):
	candidate = models.ForeignKey('candidate.Candidate')
	election = models.ForeignKey('Election')
	votes = models.IntegerField()
	def __unicode__(self):
		return self.election.name

class ElectionWinners(models.Model):
	election = models.ForeignKey(Election)
	electionsystem= models.ForeignKey(ElectionSystem)
	electionwinners = list()
	def __unicode__(self):
		return self.election.name
	

