from __future__ import unicode_literals

from django.db import models

class PostsData(models.Model):
	uid = models.CharField(max_length = 255)
	content = models.CharField(max_length = 2000)
	data = models.JSONField()
	status = models.IntegerField()

	def __unicode__(self):
		return str(self.uid)
