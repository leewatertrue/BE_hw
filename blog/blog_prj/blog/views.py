from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Post

def list(request):
    posts=Post.objects.all().order_by('-id')
    return render(request,'blog/list.html',{'posts':posts,})

def create(request):
    if request.method == "POST":
        title=request.POST.get('title')
        content=request.POST.get('content')

        post=Post.objects.create(
            title=title,
            content=content
        )
        return redirect('blog:list')
    return render(request,'blog/create.html')

def detail(request,id):
    post=get_object_or_404(Post,id=id)
    return render(request, 'blog/detail.html',{'post':post})

def update(request,id):
    post=get_object_or_404(Post,id=id)
    if request.method == 'POST':
        post.title=request.POST.get('title')
        post.content=request.POST.get('content')
        post.save()
        return redirect('blog:detail',id)
    return render(request,'blog/update.html',{'post':post})

def delete(request, id):
    post= get_object_or_404(Post, id=id)
    post.delete()
    return redirect('blog:list')