from django.contrib import admin
from .models import Artist
from .models import Festival
from .models import Performance


admin.site.register(Artist)
admin.site.register(Festival)
admin.site.register(Performance)
