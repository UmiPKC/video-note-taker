from django.db import models
from django.utils import timezone
from django.forms import ModelForm
from django.contrib.auth.models import User

# Create your models here.
class Notebook(models.Model):
	title = models.CharField(max_length=100)
	date_created = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE) 

	def __str__(self):
		return self.title

class Note(models.Model):
	timestamp = models.CharField(max_length=100, default="01:27") #for now;
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	notebook = models.ForeignKey(Notebook, on_delete=models.CASCADE)

	def __str__(self):
		show = "%s - %s" % (self.notebook, self.timestamp)
		return show

