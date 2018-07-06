from django.db import models
from divisions.models import Base, Section, SubSection 
from django.utils import timezone

class Board(Base):
	"""
		A Board can be used either as a Messaging Panel, Project or similar 
	"""
	section = models.ForeignKey(Section, related_name='board_sections', on_delete = models.PROTECT)
	subsection = models.ForeignKey(SubSection, related_name='board_sections', on_delete = models.PROTECT)
	public = models.BooleanField(default=False) # Determine if the board if for public viewing
	archived = models.BooleanField(default=False) # Determine if the board's term has expired

class Listing(Base):
	"""
		A Listing can be seen as a list of topics under the Board
	"""
	board = models.ForeignKey(Board, related_name ="listing_boards", on_delete = models.PROTECT)

class Item(Base):
	"""
		An Item can be seen as Tasks under each Listing
	"""
	Listing = models.ForeignKey(Listing, related_name ="item_listings", on_delete = models.PROTECT)

class Comment(models.Model):
	"""
		Users (Members) can get to comment on Items: A conversation
	"""
	item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='item_comments')
	comment = models.TextField()
	comment_date = models.DateTimeField(default=timezone.now)
	comment_by = models.ForeignKey('auth.User', on_delete = models.PROTECT)

	def __str__(self):
		return self.comment

class Milestone(models.Model):
	title = models.CharField(max_length=30, default='MileStone Title')
	status = models.BooleanField(default=False)
	item = models.ForeignKey(Item, on_delete=models.PROTECT)

	def __str__(self):
		return self.title