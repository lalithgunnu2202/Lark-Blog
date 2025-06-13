from django.shortcuts import render, get_object_or_404
from blog.models import *

# Create your views here.
def blogdetail_view(request,blog_id):
    blog = get_object_or_404(blog_data,id=blog_id)
    return render(request,'staticpages/detail.html',{'blog':blog})