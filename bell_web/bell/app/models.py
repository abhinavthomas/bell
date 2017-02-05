from __future__ import unicode_literals

from django.db import models

# Create your models here.
class bell(models.Model):
	"""docstring for bells"""
	name = models.CharField(max_length = 50, null=False)
	b1 = models.TimeField(blank=True, null=True)
	b2 = models.TimeField(blank=True, null=True)
	b3 = models.TimeField(blank=True, null=True)
	b4 = models.TimeField(blank=True, null=True)
	b5 = models.TimeField(blank=True, null=True)
	b6 = models.TimeField(blank=True, null=True)
	b7 = models.TimeField(blank=True, null=True)
	b8 = models.TimeField(blank=True, null=True)
	b9 = models.TimeField(blank=True, null=True)
	b10 = models.TimeField(blank=True, null=True)
	b11 = models.TimeField(blank=True, null=True)
	b12 = models.TimeField(blank=True, null=True)
	b13 = models.TimeField(blank=True, null=True)
	b14 = models.TimeField(blank=True, null=True)
	b15 = models.TimeField(blank=True, null=True)


class current(models.Model):
	"""docstring for current"""
	name = models.CharField(max_length = 50)