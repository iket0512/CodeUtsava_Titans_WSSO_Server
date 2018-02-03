from __future__ import unicode_literals

from django.db import models

# Create your models here.

class StateData(models.Model):
	name =models.CharField(max_length=100)
	def __unicode__(self):
		return self.name

class DistrictData(models.Model):
	name =models.CharField(max_length=100)
	state = models.ForeignKey(StateData,db_column='name')
	def __unicode__(self):
		return self.name

class BlockData(models.Model):
	name =models.CharField(max_length=100)
	district = models.ForeignKey(DistrictData,db_column='name')
	def __unicode__(self):
		return self.name

class PanchayatData(models.Model):
	name =models.CharField(max_length=100)
	block = models.ForeignKey(BlockData,db_column='name')
	def __unicode__(self):
		return self.name

class VillageData(models.Model):
	name =models.CharField(max_length=100)
	panchayat = models.ForeignKey(PanchayatData,db_column='name')
	def __unicode__(self):
		return self.name

class HabitationData(models.Model):
	name =models.CharField(max_length=100)
	village = models.ForeignKey(VillageData,db_column='name')

	def __unicode__(self):
		return self.name

class HabitationElementData(models.Model):
	habitation= models.ForeignKey(HabitationData,db_column='name')
	as_actual= models.FloatField(default=0)
	fe_actual= models.FloatField(default=0)
	f_actual= models.FloatField(default=0)
	salinity_actual= models.FloatField(default=0)
	nitrate_actual= models.FloatField(default=0)
	as_bis= models.FloatField(default=0)
	fe_bis= models.FloatField(default=0)
	f_bis= models.FloatField(default=0)
	salinity_bis= models.FloatField(default=0)
	nitrate_bis= models.FloatField(default=0)
	created = models.CharField(max_length=255)
	def __unicode__(self):
		return self.name


class ElementData(models.Model):
	name =models.CharField(max_length=100)
	threat_one= models.FloatField(default=0)
	threat_two= models.FloatField(default=0)
	threat_three= models.FloatField(default=0)
	threat_four= models.FloatField(default=0)
	threat_five= models.FloatField(default=0)
	hazards = models.CharField(max_length=255,null=True,blank=True)
	remedy = models.CharField(max_length=255,null=True,blank=True)
	
	def __unicode__(self):
		return self.name
		
 	


