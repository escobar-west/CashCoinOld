from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .forms import UserForm

def homepage(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/account/')
        else:
            post_error = True
    else:
        post_error = False

    form = UserForm()
    return render(request, 'home.html', {'form': form, 'post_error': post_error})


def account(request):
    return HttpResponse('Ok, {}'.format(request.user.username))
