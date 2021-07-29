from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Notebook(models.Model):
	title = models.CharField(max_length=100)
	date_created = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE) 

class Note(models.Model):
	#title
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	notebook = models.ForeignKey(Notebook, on_delete=models.CASCADE)

	def __str__(self):
		return self.content