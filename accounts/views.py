from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


def index(request):
    return HttpResponse('logged in as {}'.format(request.user.username))
