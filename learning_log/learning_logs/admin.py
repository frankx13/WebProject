from django.contrib import admin

from .models import Topic, Entry

# Register your models here.
# http://localhost:8000/admin/
admin.site.register(Topic)
admin.site.register(Entry)