from django.shortcuts import render ,get_object_or_404
from .models import*

# Create your views here.
def portolio_view(request):
    projects = Project.objects.all()
    return render(request, 'staticpages/portfolio.html',{'projects':projects})

def project_details_view(request,proj_id):
    project = get_object_or_404(Project,id=proj_id)
    return render(request, 'staticpages/project-details.html',{'project':project})
