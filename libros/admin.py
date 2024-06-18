from django.contrib import admin
from libros.models import Libros, User

# Register your models here.

admin.site.register(Libros)
admin.site.register(User)