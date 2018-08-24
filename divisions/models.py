from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from boards.models import Board
from django.urls import reverse

class Base(models.Model):
	"""
		A Base Model (Mixin Like) for the creation of Section and Team Models through Inheritance
	"""
	name = models.CharField(max_length = 50)
	description = models.TextField(blank = True)
	creator = models.ForeignKey('auth.User', on_delete = models.PROTECT)
	created = models.DateTimeField(default = timezone.now)

	class Meta:
		abstract = True

	def __str__(self):
		return self.name

class Team(Base):
	"""
		A Team can be thought of as a group:
	"""
	members = models.ManyToManyField('auth.User', related_name='team_members', blank =True)
	
	def get_absolute_url(self):
		return reverse('divisions:team-detail', kwargs={'team_id': self.pk})

class Section(Base):
	"""
		Inherits from Base and create Various Sections for use
		Each Section or sub section can have their own own teams
	"""
	teams = models.ManyToManyField(Team, related_name='section_teams', blank = True)
	members = models.ManyToManyField('auth.User', related_name='section_members', blank =True)
	boards = models.ManyToManyField('boards.Board', related_name='section_boards', blank =True)
	
	def get_absolute_url(self):
		return reverse('divisions:section-detail', kwargs={'section_id': self.pk})
