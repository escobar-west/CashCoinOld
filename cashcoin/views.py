from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .forms import UserForm, SignupForm
from accounts.models import Account
from coinbase.wallet.client import Client

def homepage_view(request):
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

def signup_view(request):
    render_di = {}

    form = SignupForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            client = Client(
                   '3tFVaskD7hLfA2b8',
                   'UFzzkgpLYSTIBYFTSgXvPaXt9KqcNKi8',
                   api_version='2017-10-29',
            )
            account = client.create_account(name="{}'s wallet".format(username))
            account_id = account['id']
            
            user = User.objects.create_user(username=username, password=password)

            new_account = Account(user=user, account_id=account_id)
            new_account.save()
            login(request, user)
            return HttpResponseRedirect('/account/')
        else:
            pass
    render_di['form'] = form
    return render(request, 'signup.html', render_di)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')
