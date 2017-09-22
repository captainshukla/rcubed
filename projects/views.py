from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

from .models import project, information
from .forms import projectForm


# Create your views here.

list_of_keys = ["abc", "xyz"]

def all_project(request):
    queryset = project.objects.all()
    info = information.objects.all().order_by('-id')[:3]
    context = {
        "object_list": queryset,
        "title": "List of All Projects",
        "info": info,
    }
    return render(request, "index.html", context)


def project_detail(request, id=None):
    instance = get_object_or_404(project, id=id)
    info = information.objects.all().order_by('-id')[:3]
    context = {
        "instance": instance,
        "info": info,
    }
    return render(request, "detail.html", context)


def add_project(request):
    form = projectForm(request.POST or None, request.FILES or None)
    info = information.objects.all().order_by('-id')[:3]

    if form.is_valid() and form.cleaned_data['project_title'] not in project.objects.all():
        if form.cleaned_data['key'] in list_of_keys:
            instance = form.save(commit=False)
            instance.save()

            queryset = project.objects.all()
            info = information.objects.all().order_by('-id')[:3]
            context = {
               "object_list": queryset,
               "title": "List of All Projects",
               "info": info,
            }
            return HttpResponseRedirect("http://127.0.0.1:8000/projects/")

        else:
            info = information.objects.all().order_by('-id')[:3]
            context = {
              "form": form,
              "Error": "Please fill out the correct ceredentials.",
              "info": info,
            }
            return render(request, "create.html", context)

    context = {
        "form": form,
        "info": info,
    }
    return render(request, "create.html", context)

def homepage(request):
    info = information.objects.all().order_by('-id')[:3]
    projects = project.objects.all()[:3]
    context = {
       "info": info,
        'object': projects,
    }
    return render(request, "index1.html", context)