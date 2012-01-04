"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from election.models import ElectionType
from election.models import Election
from election.models import ElectionResult
from election.models import ElectionSystem
from election.models import ElectionWinners
from electoralarea.models import Circunscripcion
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
		quintacosta, created = Circunscripcion.objects.get_or_create(name = 'Quinta Costa')
		eleccion = Election.objects.create(content_object = quintacosta, date=datetime.date(2011,01,01), electiontype= tipo_eleccion, name = 'municipales 2000')
		self.assertTrue(created)
		self.assertTrue(eleccion.electiontype.description=='Municipal')
		self.assertTrue(eleccion.date==datetime.date(2011,01,01))
		self.assertTrue(eleccion.content_object.name == 'Quinta Costa')
	

class AddCandidateToElection(TestCase):
	def test_add_candidate_to_a_election(self):
		#create election then add candidate through votes
		tipo_eleccion, created = ElectionType.objects.get_or_create(description = 'Senado')
		quintacosta, created = Circunscripcion.objects.get_or_create(name = 'Quinta Costa')
		eleccion = Election.objects.create(content_object = quintacosta, date=datetime.date(2011,01,01), electiontype= tipo_eleccion, name = 'municipales 2000')
		senador, created = CandidateType.objects.get_or_create(description = 'senator')
		diputado, created = CandidateType.objects.get_or_create(description = 'diputado')
		candidate1, created = Candidate.objects.get_or_create(name='candidate 1', candidatetype=senador)
		votos1, created = ElectionResult.objects.get_or_create(candidate = candidate1, election = eleccion, votes = 10)
		self.assertTrue(eleccion.electiontype.description == 'Senado')
		self.assertTrue(votos1.election.electiontype.description == 'Senado')
		self.assertTrue(votos1.candidate.candidatetype.description == 'senator')
		self.assertTrue(votos1.votes == 10)
		self.assertTrue(eleccion.candidates.get(pk=1).name == 'candidate 1')
	
	

class SetElectedCandidates(TestCase):
	def test_set_elected_candidates(self):
		#set elected candidates for an election
		tipo_eleccion, created = ElectionType.objects.get_or_create(description = 'Senado')
		quintacosta, created = Circunscripcion.objects.get_or_create(name = 'Quinta Costa')
		eleccion = Election.objects.create(content_object = quintacosta, date=datetime.date(2011,01,01), electiontype= tipo_eleccion, name = 'municipales 2000')
		senador, created = CandidateType.objects.get_or_create(description = 'senator')
		diputado, created = CandidateType.objects.get_or_create(description = 'diputado')
		candidate1, created = Candidate.objects.get_or_create(name='candidate 1', candidatetype=senador)
		candidate2, created = Candidate.objects.get_or_create(name='candidate 2', candidatetype=diputado)
		binominal, created = ElectionSystem.objects.get_or_create(description = 'binominal')
		ganadores, created = ElectionWinners.objects.get_or_create(election = eleccion, electionsystem = binominal)
		ganadores.electionwinners.append(candidate2)
		self.assertTrue(ganadores.electionwinners.pop().name == 'candidate 2')
	
