from django.contrib import admin

# Register your models here.
from .models import Contact,Promote

admin.site.register(Contact),
admin.site.register(Promote)
