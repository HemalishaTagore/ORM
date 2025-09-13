from django.contrib import admin
from .models import Cars_DB, Cars_DBAdmin
admin.site.register(Cars_DB, Cars_DBAdmin)