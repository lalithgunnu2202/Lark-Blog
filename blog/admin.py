from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(blog_data)
admin.site.register(Tag)
admin.site.register(Author)