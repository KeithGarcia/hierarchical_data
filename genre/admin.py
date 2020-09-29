from django.contrib import admin

from mptt.admin import MPTTModelAdmin , DraggableMPTTAdmin

from genre.models import Genre

admin.site.register(Genre, DraggableMPTTAdmin)