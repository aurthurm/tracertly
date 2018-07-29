from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from boards.models import Board

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
	pass

class Section(Base):
	"""
		Inherits from Base and create Various Sections for use
		Each Section or sub section can have their own own teams
	"""
	teams = models.ManyToManyField(Team, related_name='section_teams', blank = True)
	members = models.ManyToManyField(User, related_name='section_members', blank =True)
	boards = models.ManyToManyField(Board, related_name='section_boards', blank =True)

class SubSection(Base):	
	"""
		A Section can have sections within itself (sub sections)
		Each SubSection belongs to a Section
	"""
	mainSection = models.ForeignKey(Section, related_name ='main_section', on_delete = models.PROTECT, blank = False)
	teams = models.ManyToManyField(Team, related_name='subsection_teams', blank = True)


class SubTeam(Base):	
	"""
		A Team can have small teams within itself (sub teams)
		Each SubTeam belongs to a Team
	"""
	mainTeam = models.ForeignKey(Team, related_name ='main_team', on_delete = models.PROTECT, blank = False)
