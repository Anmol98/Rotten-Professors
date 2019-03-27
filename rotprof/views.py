from django.shortcuts import render, get_object_or_404, redirect
from .models import Professor
from .forms import  CommentForm

def branch_list(request):
    return render(request, 'rotprof/branch_list.html', {})

def prof_list_branch(request, branch):
    posts = Professor.objects.filter(Branch = branch)
    return render(request, 'rotprof/prof_list_branch.html', {'posts' : posts})


def prof_detail(request, pk, bran):
    post = Professor.objects.get(pk=pk, Branch=bran)
    return render(request, 'rotprof/prof_detail.html', {'post': post})


def add_comment_to_post(request, pk, bran):
    post = get_object_or_404(Professor, pk=pk, Branch=bran)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('prof_list_branch', bran)
    else:
        form = CommentForm()
    return render(request, 'rotprof/add_comment_to_post.html', {'form': form})
