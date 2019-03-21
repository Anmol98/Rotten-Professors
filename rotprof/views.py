from django.shortcuts import render
from .models import Professor

def branch_list(request):
    return render(request, 'rotprof/branch_list.html', {})

def prof_list_branch(request, pk):
    posts = Professor.objects.filter(Branch = pk)
    return render(request, 'rotprof/prof_list_branch.html', {'posts' : posts})
