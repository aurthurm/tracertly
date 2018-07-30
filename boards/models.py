from django.db import models
from divisions.models import *
from django.utils import timezone
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

class Board(Base):
	"""
		A Board can be used either as a Messaging Panel, Project or similar 
	"""
	section = models.ForeignKey('divisions.Section', related_name='board_sections', on_delete = models.PROTECT)
	subsection = models.ForeignKey('divisions.SubSection', blank = True, null = True, related_name='board_sections', on_delete = models.PROTECT)
	public = models.BooleanField(default=False) # Determine if the board if for public viewing
	archived = models.BooleanField(default=False) # Determine if the board's term has expired

	def get_absolute_url(self):
		return reverse('boards:board-detail', kwargs={'board_id': self.pk})

class Listing(Base):
	"""
		A Listing can be seen as a list of topics under the Board
	"""
	board = models.ForeignKey(Board, related_name ="listing_boards", on_delete = models.PROTECT)

	def get_absolute_url(self):
		# return reverse('boards:listing-detail', kwargs={'board_id': self.board.pk, 'listing_id': self.pk})
		return reverse('boards:board-detail', kwargs={'board_id': self.board.pk})

class Item(Base):
	"""
		An Item can be seen as Tasks under each Listing
	"""
	Listing = models.ForeignKey(Listing, related_name ="item_listings", on_delete = models.PROTECT)
		
	def get_absolute_url(self):
		return reverse('boards:board-detail', kwargs={'board_id': self.Listing.board.pk})

class Comment(models.Model):
	"""
		Users (Members) can get to comment on Items: A conversation
	"""
	item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='item_comments')
	comment = models.TextField()
	comment_date = models.DateTimeField(default=timezone.now)
	comment_by = models.ForeignKey('auth.User', on_delete = models.PROTECT)
	
	class Meta:
		ordering = ('-comment_date',)

	def __str__(self):
		return self.comment
	
	def get_absolute_url(self):
		return reverse('boards:item-detail', kwargs={'board_id': self.item.Listing.board.pk, 'listing_id': self.item.Listing.pk, 'item_id': self.item.pk})

class Milestone(models.Model):
	title = models.CharField(max_length=30, default='MileStone Title')
	status = models.BooleanField(default=False)
	item = models.ForeignKey(Item, on_delete=models.PROTECT)
	creator = models.ForeignKey('auth.User', on_delete = models.PROTECT)

	def __str__(self):
		return self.title
	
	def get_absolute_url(self):
		return reverse('boards:item-detail', kwargs={'board_id': self.item.Listing.board.pk, 'listing_id': self.item.Listing.pk, 'item_id': self.item.pk})