"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from division_electoral.models import Circunscripcion
from division_electoral.models import District
from division_electoral.models import Comuna
from division_electoral.models import Region

class CircuscripcionTest(TestCase):
	def test_create_circunscripcion(self):
		#create circunscripcion from scratch
		circunscripcion, created = Circunscripcion.objects.get_or_create(name='circunscripcion 1')
		self.assertTrue(created)
		self.assertTrue(circunscripcion.name=='circunscripcion 1')
	
class DistrictTest(TestCase):
	def test_create_district(self):
		#create district from scratch
                circunscripcion = Circunscripcion.objects.create(name='circunscripcion 1')
		district = District.objects.create(name='district 1',circunscripcion = circunscripcion)
		self.assertIsNotNone(district.pk)
		self.assertTrue(district.name=='district 1')
                self.assertEqual(district.circunscripcion, circunscripcion)


class RegionTest(TestCase):
	def test_create_region(self):
		#create region from scratch
		region, created = Region.objects.get_or_create(name='region 1')
		self. assertTrue(created)
		self.assertTrue(region.name=='region 1')
		
class ComunaTest(TestCase):
	def test_create_comuna(self):
		#create comuna from scratch
                circunscripcion = Circunscripcion.objects.create(name='circunscripcion 1')
		district, created = District.objects.get_or_create(name='district 1', circunscripcion = circunscripcion)
		region, created = Region.objects.get_or_create(name='region 1')
		comuna, created = Comuna.objects.get_or_create(name='comuna 1', region = region, district = district)
		self.assertTrue(created)
		self.assertTrue(comuna.name=='comuna 1')
		self.assertTrue(comuna.region.name == 'region 1')
		self.assertTrue(comuna.district.name == 'district 1')
