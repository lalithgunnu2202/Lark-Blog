from django.shortcuts import render
from .models import*

# Create your views here.
def home_view(request):
    blogs = blog_data.objects.all()[:3]
    return render(request,'home.html',{'blogs':blogs})