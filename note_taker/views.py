from django.shortcuts import render
from django.views.generic import CreateView
from django.http import HttpResponseRedirect
import random

from .models import Notebook, Note
from .forms import NoteForm, NotebookForm

#admin, testing321

# Create your views here.
def home(request):
	pass
	#future landing/home page

def notebook(request):
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

	return render(request, 'note_taker/dev_land.html', context)

def new_notebook(request):
	if request.method == 'POST':
		form = NotebookForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(request.path_info)
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
	#future notebook creation page
	#update Notebook model to include field for youtube link
	return render(request, 'note_taker/new_notebook.html', context)

def my_notebooks(request):
	pass
	#future user notebooks page



def dev_homepage(request):
	context = {
		'notebook': Notebook.objects.all(),
	}

	return render(request, 'note_taker/dev_land.html', context)

def test_notebook(request, id_num):
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



#def new_note(request):
#	if request.method == 'POST':
#		form = NoteForm(request.POST)
#		if form.is_valid():
#			return HttpResponseRedirect('')
#	else:
#		form = NoteForm()	
#	return render(request, 'note_taker/note_form.html', { 'form': form })


#class NoteCreate(CreateView):
#	model = Note
#	fields = ['timestamp', 'content', 'notebook']
	#template_name = "note_taker/note_form.html"
#	template_name = "note_taker/index.html"