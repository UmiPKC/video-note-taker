from django import forms
from .models import Note, Notebook

class NoteForm(forms.Form):
	class Meta:
		model = Note
		fields = ['timestamp', 'content']