from django.urls import path
from . import views
#from .views import NoteCreate

urlpatterns = [
	#path('', views.home, name="note-taker-home"),
	path('', views.notebook, name="note-taker-notebook"),
	path('notebook/<str:id_num>/', views.test_notebook, name="note-taker-notebook-test"),
	path('new/', views.new_notebook, name="notebook-new"),

]

#path('note/new/', NoteCreate.as_view(), name='note-taker-create'),
#path('note/new/', views.new_note, name='note-taker-create'),