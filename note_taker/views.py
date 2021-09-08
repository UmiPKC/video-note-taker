from django.shortcuts import render
from django.views.generic import CreateView
from django.http import HttpResponseRedirect

from .models import Notebook, Note
from .forms import NoteForm

#admin, testing321

# Create your views here.
def home(request):
	if request.method == 'POST':
		form = NoteForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(request.path_info)
	else:
		form = NoteForm()	

	context = {
		'notebook': Notebook.objects.all().first(),
		'notes': Note.objects.all(),
		'form': form,
	}

	return render(request, 'note_taker/index.html', context)


def new_note(request):
	if request.method == 'POST':
		form = NoteForm(request.POST)
		if form.is_valid():
			return HttpResponseRedirect('')
	else:
		form = NoteForm()	

	return render(request, 'note_taker/note_form.html', { 'form': form })


class NoteCreate(CreateView):
	model = Note
	fields = ['timestamp', 'content', 'notebook']
	#template_name = "note_taker/note_form.html"
	template_name = "note_taker/index.html"