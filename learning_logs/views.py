from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm, EntryForm


def index(request):
    posts=Post.objects.order_by('-created')
    context = {'posts':posts,}
    return render(request, 'learning_logs/index.html',context)

def image(request, post_id):
    imag = Post.objects.get(id=post_id)
    entries = imag.entry_set.order_by('-date_added')
    if request.method!='POST':
        form=EntryForm()
    else:
        form=EntryForm(data=request.POST)
        if form.is_valid():
            new_entry=form.save(commit=False)
            new_entry.topic=imag
            new_entry.save()
            return redirect('learning_logs:image', post_id=post_id)


    context = {'imag': imag, 'entries': entries,'form':form}
    return render(request, 'learning_logs/image.html', context)

def new_post(request):
    if request.method != 'POST':
        form=PostForm()
    else:
        form=PostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()

            return redirect('learning_logs:index')

    context = {'form': form}
    return render(request, 'learning_logs/new_post.html', context)


