from django.urls import path
from . import views

urlpatterns = [
	#homepage notebook list view
	path('', views.notebook_list, name="note-taker-notebook-list"),
	#notebook detail view
	path('notebook/<str:id_num>/', views.notebook, name="note-taker-notebook"),
	#new notebook page
	path('new/', views.new_notebook, name="notebook-new"),
	#delete notebook
	path('delete-notebook/<int:id>/', views.delete_notebook, name="delete-notebook"),
	#delete note
	path('delete-note/<int:id>/', views.delete_note, name="delete-note"),

]
