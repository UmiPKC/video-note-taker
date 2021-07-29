from django.contrib import admin
from .models import Notebook, Note

# Register your models here.
admin.site.register(Notebook)
admin.site.register(Note)