from django.db import models

# Create your models here.
class Candidate(models.Model):
	name=models.CharField(max_length = 200)
	type=models.ForeignKey('CandidateType')
class CandidateType(models.Model):
	description=models.CharField(max_length = 200)
	