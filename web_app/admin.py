from django.contrib import admin
from .models import expenses,Question,Choice

# Register your models here.
admin.site.register(expenses)
admin.site.register(Question)
admin.site.register(Choice)
