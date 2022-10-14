from atexit import register
from django.contrib import admin
from Django_app.models import account_info
# Register your models here.
admin.site.register(account_info)