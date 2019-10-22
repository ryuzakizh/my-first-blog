from django.contrib import admin

# Register your models here.
from .models import Post

admin.site.register(Post) #to make a model visible on the admin page