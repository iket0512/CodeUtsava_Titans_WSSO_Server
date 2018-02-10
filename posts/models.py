from __future__ import unicode_literals

from django.db import models
from jsonfield import JSONField

from data.models import HabitationData

class PostsData(models.Model):
	uid = models.CharField(max_length = 255)
	content = models.CharField(max_length = 2000)
	data = JSONField()
	status = models.IntegerField()
	habitation = models.ForeignKey(HabitationData)

	def __unicode__(self):
		return str(self.uid)

class ExtendedHabitationElementsData(models.Model):
	habitation = models.ForeignKey(HabitationData)
	latitude = models.DecimalField(max_digits = 15, decimal_places = 8, default = 0)
	longitude = models.DecimalField(max_digits = 15, decimal_places = 8, default = 0)
	f_l = models.DecimalField(default = 0, max_digits = 8, decimal_places = 2) 
	as_l = models.DecimalField(default = 0, max_digits = 8, decimal_places = 2)
	fe_l = models.DecimalField(default = 0, max_digits = 8, decimal_places = 2)
	n_l = models.DecimalField(default = 0, max_digits = 8, decimal_places = 2)
	s_l = models.DecimalField(default = 0, max_digits = 8, decimal_places = 2)
	f_al = models.DecimalField(default = 0, max_digits = 8, decimal_places = 2)
	as_al = models.DecimalField(default = 0, max_digits = 8, decimal_places = 2)
	fe_al = models.DecimalField(default = 0, max_digits = 8, decimal_places = 2)
	n_al = models.DecimalField(default = 0, max_digits = 8, decimal_places = 2)
	s_al = models.DecimalField(default = 0, max_digits = 8, decimal_places = 2)
	f_count = models.DecimalField(default = 0, decimal_places = 2, max_digits = 5)
	fe_count = models.DecimalField(default = 0, decimal_places = 2, max_digits = 5)
	as_count = models.DecimalField(default = 0, decimal_places = 2, max_digits = 5)
	n_count = models.DecimalField(default = 0, decimal_places = 2, max_digits = 5)
	s_count = models.DecimalField(default = 0, decimal_places = 2, max_digits = 5)
	created = models.DateField()
	class Meta:
		managed = False

	@property
	def alert_level(self):
		return max(self.f_al, self.as_al, self.fe_al, self.n_al, self.s_al)