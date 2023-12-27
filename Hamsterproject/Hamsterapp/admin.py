from django.contrib import admin

from .models import FormUser

class FormUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'age',]
    list_display_links = ['name', 'email',]
    list_filter = ['age',]

admin.site.register(FormUser, FormUserAdmin)