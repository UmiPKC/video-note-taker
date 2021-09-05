from django.shortcuts import render
from django.views.generic import CreateView
from django.http import HttpResponseRedirect

from .models import Notebook, Note
from .forms import NoteForm


# Create your views here.
def home(request):
	if request.method == 'POST':
		form = NoteForm(request.POST)
		if form.is_valid():
			return HttpResponseRedirect('')
	else:
		form = NoteForm()	

	context = {
		'notebook': Notebook.objects.all().first(),
		'notes': Note.objects.all(),
		'form': form,
	}

	return render(request, 'note_taker/index.html', context)



class NoteCreate(CreateView):
	model = Note
	fields = ['timestamp', 'content', 'notebook']
	template_name = "note_taker/index.html"
	