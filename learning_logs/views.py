from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm, EntryForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    posts=Post.objects.order_by('-created')
    paginator = Paginator(posts, 18)  # По 3 статьи на каждой странице.
    page = request.GET.get('page')


    try:
        posts = paginator.get_page(page)
    except PageNotAnInteger:
        # Если страница не является целым числом, возвращаем первую страницу.
        posts = paginator.page(1)
    except EmptyPage:
    # Если номер страницы больше, чем общее количество страниц, возвращаем последнюю.
        posts = paginator.page(paginator.num_pages)

    context = {'posts':posts,'page':page}
    return render(request, 'learning_logs/index.html',context)

@login_required
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
            new_entry.aftor = request.user
            new_entry.save()
            return redirect('learning_logs:image', post_id=post_id)


    context = {'imag': imag, 'entries': entries,'form':form}
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


