from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login
from users.forms import MyForm


def register(request):
    if request.method != "POST":
        form = MyForm()
    else:
        form = MyForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('learning_logs:index')
    context = {'form': form}
    return render(request, 'users/registration/register.html', context)
