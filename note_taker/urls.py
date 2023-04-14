from django.urls import path
from . import views

urlpatterns = [
	path('', views.notebook_list, name="note-taker-notebook-list"),
	path('notebook/<str:id_num>/', views.notebook, name="note-taker-notebook"),
	path('new/', views.new_notebook, name="notebook-new"),

]
