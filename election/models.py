from django.db import models
from candidate.models import Candidate
import datetime

# Create your models here.
class ElectionType(models.Model):
	description = models.CharField(max_length = 200)
class Election(models.Model):
	type = models.ForeignKey('ElectionType')
	date = models.DateField()
	candidate = models.ManyToManyField('candidate.Candidate')
	# def AddCandidate(candidate):
	# 	candidates.append(candidate)