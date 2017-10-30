#!/Users/escobar/anaconda/bin/python
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .forms import UserForm, SignupForm

def homepage(request):
    render_di = {} 
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/account/')
        else:
            render_di['post_error'] = True
    else:
        render_di['post_error'] = False

    render_di['form'] = UserForm()
    return render(request, 'home.html', render_di)

def signup(request):
    render_di = {}
    render_di['form'] = SignupForm()
    return render(request, 'signup.html', render_di)
