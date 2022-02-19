from django.shortcuts import render
from main_page.models import Project

def main_page(request):
    projects = Project.objects.all()
    return render(request, 'main_page.html', {'projects':projects})

