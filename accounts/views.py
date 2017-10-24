from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Account
from coinbase.wallet.client import Client

client = Client(
        'hRL0pNmbKE1Hp53L',
        'nMgTROfkrKOZVfCKCGyBzVUsFpoNIetd',
        api_version='2017-10-17',)


def index(request):
    account = Account.objects.filter(user=request.user)[0]
    print(account)
    print(account.account_id)
    balance = client.get_account(account.account_id).balance.amount
    return HttpResponse('logged in as {} with a balance of {} ETH'
                           .format(request.user.username, balance)
                       )
    
