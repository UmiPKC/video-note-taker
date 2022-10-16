from django.db import models
from django.utils import timezone
from django.forms import ModelForm
from django.contrib.auth.models import User

# Create your models here.
class Notebook(models.Model):
	title = models.CharField(max_length=100)
	date_created = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE) 
	youtube_id = models.CharField(max_length=100, default="Will fill automatically") #youtube ID #default is furret vid
	notebook_id = models.CharField(max_length=100, default='Randomly generated') #randomly generated id
	description = models.CharField(max_length=500, default=None, blank=True, null=True)
	#game_id = models.ForeignKey(Game, on_delete=models.CASCADE)
	privacy = models.CharField(max_length=100, default="Private") #Private or Public

	def __str__(self):
		return "%s, Youtube ID: %s, Notebook ID: %s" % (self.title, self.youtube_id, self.notebook_id)

class Note(models.Model):
	timestamp = models.CharField(max_length=100, default="01:27") #for now;
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	notebook = models.ForeignKey(Notebook, on_delete=models.CASCADE)
	likes = models.IntegerField(default=0)


	def __str__(self):
		show = "%s - %s" % (self.notebook, self.timestamp)
		return show

