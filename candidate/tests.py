"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from candidate.models import Candidate
from candidate.models import CandidateType

class TypeTest(TestCase):
	def test_create_type(self):
		#create type of candidate
		tipo, created = CandidateType.objects.get_or_create(description = 'senator')
		self.assertTrue(created)
		self.assertTrue(tipo.description=='senator')
		
class CandidateTest(TestCase):
	def test_create_candidate(self):
		#create candiate from scratch
		senador, created = CandidateType.objects.get_or_create(description = 'senator')
		candidate, created = Candidate.objects.get_or_create(name='candidate 1', type=senador)
		self.assertTrue(created)
		self.assertTrue(candidate.name=='candidate 1')
		self.assertTrue(candidate.type.description=='senator')