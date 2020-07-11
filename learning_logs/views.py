from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm


def index(request):
    posts=Post.objects.all()
    context = {'posts':posts,}
    return render(request, 'learning_logs/index.html',context)

def image(request, post_id):
    imag = Post.objects.get(id=post_id)
    entries = imag.entry_set.order_by('-date_added')
    context = {'imag': imag, 'entries': entries}
    return render(request, 'learning_logs/image.html', context)

def new_post(request):
    if request.method!='Post':
        form=PostForm()
    else:
        form=PostForm(data=request.POST)
        if form.is_valid:
            form.save()
            return render('learning_logs:image')
    context = {'form': form}
    return render(request, 'learning_logs/new_post.html', context)
