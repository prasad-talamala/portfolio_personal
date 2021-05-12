from django.shortcuts import render
from .models import Project


def home(request):
    all_projects = Project.objects.all()
    return render(request, "home.html", {"projects": all_projects})
