from django.contrib import admin

from hello.models import Category, Page


admin.site.register(Category)
admin.site.register(Page)