from django.urls import path
from . import views
from .views import NoteCreate

urlpatterns = [
	path('', views.home, name="note-taker-home"),
	path('note/new/', NoteCreate.as_view(), name='note-taker-create'),
]