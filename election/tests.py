"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from election.models import ElectionType
from election.models import Election
from candidate.models import Candidate
from candidate.models import CandidateType
import datetime


class ElectionTypeTest(TestCase):
	def test_create_type_of_elecction(self):
		#create type of election
		tipo_eleccion, created = ElectionType.objects.get_or_create(description = 'Municipal')
		self.assertTrue(created)
		self.assertTrue(tipo_eleccion.description=='Municipal')
class ElectionTest(TestCase):
	def test_create_election(self):
		#create election
		tipo_eleccion, created = ElectionType.objects.get_or_create(description = 'Municipal')
		eleccion, created = Election.objects.get_or_create(date=datetime.date(2011,01,01), type= tipo_eleccion)
		self.assertTrue(created)
		self.assertTrue(eleccion.type.description=='Municipal')
		self.assertTrue(eleccion.date==datetime.date(2011,01,01))
class AddCandidateToElection(TestCase):
	def test_add_candidate_to_a_election(self):
		#create election then add candidate
		tipo_eleccion, created = ElectionType.objects.get_or_create(description = 'Senado')
		eleccion, created = Election.objects.get_or_create(date=datetime.date(2011,01,01), type= tipo_eleccion)
		senador, created = CandidateType.objects.get_or_create(description = 'senator')
		candidate, created = Candidate.objects.get_or_create(name='candidate 1', type=senador)
		eleccion.candidates=candidate
		self.assertTrue(eleccion.candidates(0).name == 'candidate 1')
	
