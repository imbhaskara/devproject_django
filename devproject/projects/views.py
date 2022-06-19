from django.shortcuts import render
#import Model kita ke dalam views
from .models import Project


# Create your views here.
def projects(request):
    projects = Project.objects.all()
    context = {'projects':projects}
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    project = Project.objects.get(id=pk)
    return render(request, 'projects/single-project.html', {'project':project})
