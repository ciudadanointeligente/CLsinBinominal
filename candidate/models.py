from django.db import models

# Create your models here.
class Candidate(models.Model):
	name=models.CharField(max_length = 200)
	candidatetype=models.ForeignKey('CandidateType')
	def __unicode__(self):
		return self.name
class CandidateType(models.Model):
	description=models.CharField(max_length = 200)
	def __unicode__(self):
		return self.description
	