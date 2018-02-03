from __future__ import unicode_literals

from django.db import models

class CommentsData(models.Model):
	post_id=models.CharField(max_length=500,null=False)
	user_id=models.CharField(max_length=500,null=False)
	user_post_id=models.CharField(max_length=500,null=False)
	created = models.DateTimeField(auto_now = False, auto_now_add = True)
	def __unicode__(self):
		return str(self.user_post_id)

class UserComments(models.Model):
	user_post_id=models.ForeignKey(CommentsData)
	text=models.CharField(max_length=500)
	created = models.DateTimeField(auto_now = False, auto_now_add = True)
	def __unicode__(self):
		return str(self.user_post_id)

