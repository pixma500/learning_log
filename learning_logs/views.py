from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm, EntryForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.views.decorators.http import require_POST


def home(request):
    return render(request,'learning_logs/base.html')

def index(request):
    post=Post.objects.order_by('-created')
    paginator = Paginator(post, 16)
    page = request.GET.get('page')
    try:
        posts = paginator.get_page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {'posts':posts,'page':page,'post':post}
    return render(request, 'learning_logs/index.html',context)



def image(request, post_id):
    imag = Post.objects.get(id=post_id)
    entries = imag.entry_set.order_by('-date_added')
    l=len(entries)
    k=l%2
    if request.method!='POST':
        form=EntryForm()
    else:
        form=EntryForm(data=request.POST)
        if form.is_valid():
            new_entry=form.save(commit=False)
            new_entry.topic=imag
            new_entry.aftor = request.user
            new_entry.save()
            return redirect('learning_logs:image', post_id=post_id)

    context = {'imag': imag, 'entries': entries, 'form': form,'l':l,'k':k}
    return render(request, 'learning_logs/image.html', context)

@login_required
def new_post(request):
    if request.method != 'POST':
        form=PostForm()
    else:
        form=PostForm(request.POST,request.FILES)
        if form.is_valid():
            new_imeg = form.save(commit=False)
            new_imeg.owner = request.user
            new_imeg.save()

            return redirect('learning_logs:index')

    context = {'form': form}
    return render(request, 'learning_logs/new_post.html', context)

@login_required
@require_POST
def image_like(request):
    image_id = request.POST.get('id')
    action = request.POST.get('action')
    if image_id and action:
        try:
            image =Post.objects.get(id=image_id)

            if action == 'like':
                image.users_like.add(request.user)
            else:
                image.users_like.remove(request.user)
            return JsonResponse({'status':'ok'})
        except:
            pass
    return JsonResponse({'status':'ok'})


