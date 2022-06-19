from django.shortcuts import render
from django.http import HttpResponse

projectsList = [
    {
        'id': 1,
        'title': 'Ecommerce Website',
        'description': 'This is a ecommerce website',
    },
    {
        'id': 2,
        'title': 'Porfolio Website',
        'description': 'This was a project where I built a portfolio website',
    },
    {
        'id': 3,
        'title': 'Social Network Website',
        'description': 'Awesome open source social network website project I am still working on',
    },
]

# Create your views here.
def projects(request):
    number = 7
    context = {'number':number, 'projects':projectsList}
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    projectObj = None
    for i in projectsList:
        if i['id'] == pk:
             projectObj = i
    return render(request, 'projects/single-project.html', {'project':projectObj})
