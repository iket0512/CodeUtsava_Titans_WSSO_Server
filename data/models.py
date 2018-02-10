from __future__ import unicode_literals

from django.db import models

# Create your models here.

class StateData(models.Model):
	name = models.CharField(max_length = 254)
	def __unicode__(self):
		return str(self.name)

class DistrictData(models.Model):
	name = models.CharField(max_length = 254)
	state = models.ForeignKey(StateData)
	def __unicode__(self):
		return str(self.name)

class BlockData(models.Model):
	name = models.CharField(max_length = 254)
	district = models.ForeignKey(DistrictData)
	def __unicode__(self):
		return str(self.name)

class PanchayatData(models.Model):
	name = models.CharField(max_length = 254)
	block = models.ForeignKey(BlockData)
	def __unicode__(self):
		return str(self.name)

class VillageData(models.Model):
	name = models.CharField(max_length = 254)
	panchayat = models.ForeignKey(PanchayatData)
	def __unicode__(self):
		return str(self.name)

class HabitationData(models.Model):
	name = models.CharField(max_length = 254)
	village = models.ForeignKey(VillageData)
	latitude = models.DecimalField(max_digits = 15, decimal_places = 8, default = 0)
	longitude = models.DecimalField(max_digits = 15, decimal_places = 8, default = 0)
	def __unicode__(self):
		return str(self.name)

class ElementData(models.Model):
	name = models.CharField(max_length = 255)
	hazards = models.CharField(max_length = 1500, null = True, blank = True)
	remedy = models.CharField(max_length = 1500, null = True, blank = True)
	permissible_limit_low = models.DecimalField(default = 0, max_digits = 8, decimal_places = 2)
	permissible_limit_high = models.DecimalField(default = 0, max_digits = 8, decimal_places = 2)	
	def __unicode__(self):
		return str(self.name)

class HabitationElementData(models.Model):
	habitation = models.ForeignKey(HabitationData)
	element = models.ForeignKey(ElementData)
	count = models.DecimalField(default = 0, decimal_places = 2, max_digits = 5)
	created = models.DateField()
	def __unicode__(self):
		return str(self.habitation)

class Officials(models.Model):
	name = models.CharField(max_length = 254)
	department = models.CharField(max_length = 254)
	designation = models.CharField(max_length = 254)
	location = models.CharField(max_length = 254)
	email = models.EmailField(max_length = 254)
	mobile = models.CharField(max_length = 11)
	block = models.ForeignKey(BlockData)


# class ExtendedHabitationElementData(models.Model):
# 	name = models.CharField(max_length = 255)
# 	village = models.ForeignKey(VillageData)
# 	latitude = models.DecimalField(max_digits = 15, decimal_places = 8, default = 0)
# 	longitude = models.DecimalField(max_digits = 15, decimal_places = 8, default = 0)
# 	alert_level = models.IntegerField(default = 0)
# 	f_al = models.IntegerField(default = 0)
# 	f_l = models.DecimalField(max_digits = 8, default = 0, decimal_places = 2)
# 	as_al = models.IntegerField(default = 0)
# 	as_l = models.DecimalField(max_digits = 8, default = 0, decimal_places = 2)
# 	fe_al = models.IntegerField(default = 0)
# 	fe_l = models.DecimalField(max_digits = 8, default = 0, decimal_places = 2)
# 	n_al = models.IntegerField(default = 0)
# 	n_l = models.DecimalField(max_digits = 8, default = 0, decimal_places = 2)
# 	sl_al = models.IntegerField(default = 0)
# 	sl_l = models.DecimalField(max_digits = 8, default = 0, decimal_places = 2)
# 	address = models.CharField(max_length = 2000)

# 	class Meta:
# 		managed = False
