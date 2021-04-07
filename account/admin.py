from django.contrib import admin
from .models import Account, History

@admin.register(Account)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(History)
class AuthorAdmin(admin.ModelAdmin):
    pass