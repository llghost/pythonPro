from django.contrib import admin

from .models import Post,Content
# Register your models here.
admin.site.register((Post,Content)) #注册应用