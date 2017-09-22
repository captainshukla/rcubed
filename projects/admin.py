from django.contrib import admin

# Register your models here.
from .models import project, information

admin.site.register(project)
admin.site.register(information)