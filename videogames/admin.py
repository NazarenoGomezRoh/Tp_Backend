from django.contrib import admin
from videogames.models import Videogames, User

# Register your models here.

admin.site.register(Videogames)
admin.site.register(User)