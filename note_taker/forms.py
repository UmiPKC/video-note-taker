from django.forms import ModelForm
from .models import Note, Notebook

class NoteForm(ModelForm):
	#timestamp = forms.CharField(max_length=100)
	#content = forms.CharField(widget=forms.Textarea)
	#notebook = forms.CharField(max_length=100)
	class Meta:
		model = Note
		fields = ['timestamp', 'raw_timestamp', 'content', 'date_posted', 'notebook']

#Create NoteBookForm
class NotebookForm(ModelForm):
	class Meta:
		model = Notebook
		fields = ['title', 'author', 'youtube_id', 'notebook_id', 'description'] #'youtube_id'