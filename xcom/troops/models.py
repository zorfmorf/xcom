from django.db import models

# Create your models here.

class Role(models.Model):
	name = models.CharField(max_length = 50)
	def __str__(self):
		return self.name

class Rank(models.Model):
	name = models.CharField(max_length = 50)
	def __str__(self):
		return self.name
	
class Status(models.Model):
	name = models.CharField(max_length = 50)
	def __str__(self):
		return self.name

class Squad(models.Model):
	name = models.CharField(max_length = 100)
	joined = models.DateField('Established')
	def __str__(self):
		return self.name

class Soldier(models.Model):
	name = models.CharField(max_length = 100)
	joined = models.DateField('Joined')
	squad = models.ForeignKey(Squad)
	role = models.ForeignKey(Role)
	rank = models.ForeignKey(Rank)
	status = models.ForeignKey(Status)
	def __str__(self):
		return self.name
	def joinDate(self):
		return self.joined.strftime('%d/%m/%Y')

class SoldierEvent(models.Model):
	soldier = models.ForeignKey(Soldier)
	date = models.DateField('Date')
	event = models.CharField(max_length = 200)

class MissionType(models.Model):
	name = models.CharField(max_length = 100)
	def __str__(self):
		return self.name

class MissionResult(models.Model):
	name = models.CharField(max_length = 50)
	def __str__(self):
		return self.name

class Mission(models.Model):
	name = models.CharField(max_length = 100)
	missionType = models.ForeignKey(MissionType)
	date = models.DateField('Date')
	squad = models.ForeignKey(Squad)
	result = models.ForeignKey(MissionResult)
	wounded = models.IntegerField(default=0)
	dead = models.IntegerField(default=0)
	def __str__(self):
		return self.name
	def missionDate(self):
		return self.date.strftime('%d/%m/%Y')

# log geoscape events (build x, shot down ufo, etc)
class Event(models.Model):
	name = models.CharField(max_length = 100)
	date = models.DateField('Date')
	def __str__(self):
		return self.name
