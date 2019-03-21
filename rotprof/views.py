from django.shortcuts import render
from .models import Professor

def branch_list(request):
    return render(request, 'rotprof/branch_list.html', {})

def prof_list_branch(request, branch):
    posts = Professor.objects.filter(Branch = branch)
    return render(request, 'rotprof/prof_list_branch.html', {'posts' : posts})
def prof_detail(request, pk, bran):
    post = Professor.objects.get(pk=pk, Branch=bran)
    return render(request, 'rotprof/prof_detail.html', {'post': post})
