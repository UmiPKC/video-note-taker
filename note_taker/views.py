from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.http import HttpResponseRedirect
import random

from .models import Notebook, Note
from .forms import NoteForm, NotebookForm

#administrator/umi, testing321

# Create your views here.
def notebook_list(request):
	if request.method == 'POST':
		form = NoteForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(request.path_info)
	else:
		form = NoteForm()	

	context = {
		'notebook': Notebook.objects.all(),
		'notes': Note.objects.all(),
		'form': form,
	}

	return render(request, 'note_taker/notebook_list.html', context)


def notebook(request, id_num):
	if request.method == 'POST':
		form = NoteForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(request.path_info)
	else:
		form = NoteForm()	

	def find_notebook(id_num):
		for book in Notebook.objects.all():
			if book.notebook_id == id_num:
				return book

	def find_notes(id_num):
		return Note.objects.all().filter(notebook=find_notebook(id_num))

	context = {
		'notebook': find_notebook(id_num),#Notebook.objects.all(),
		'notes': find_notes(id_num),
		'form': form,
	}

	return render(request, 'note_taker/notebook.html', context)


def new_notebook(request):
	if request.method == 'POST':
		form = NotebookForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/")
	else:
		form = NotebookForm()

	def new_id():
		random_id = ""
		for i in range(0, 4):
			random_id += chr(random.randint(48, 57))
			random_id += chr(random.randint(65, 90))
			random_id += chr(random.randint(97, 122))
			return random_id

	context = {
		'form': form,
		'random_id': new_id(),
	}
	return render(request, 'note_taker/new_notebook.html', context)

def delete_notebook(request, id):
	notebook = Notebook.objects.get(id=id)
	notebook.delete()
	return redirect("note-taker-notebook-list")

def delete_note(request, id):
	note = Note.objects.get(id=id)
	note.delete()
	#I'm close to redirecting to the current notebook. Need a way to get the correct notebook ID so i can redirect to the right page
	return redirect("note-taker-notebook", note.notebook_id)