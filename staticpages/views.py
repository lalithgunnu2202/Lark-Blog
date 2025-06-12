from django.shortcuts import render
from blog.models import *

# Create your views here.
def all_blogs_view(request):
    blogs = blog_data.objects.all()
    return render(request, 'allblogs.html',{'blogs':blogs})
