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