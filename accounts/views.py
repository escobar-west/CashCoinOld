from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Account
from coinbase.wallet.client import Client

client = Client(
        'hRL0pNmbKE1Hp53L',
        'nMgTROfkrKOZVfCKCGyBzVUsFpoNIetd',
        api_version='2017-10-17',)

@login_required
def account_view(request):
    render_di = {}
    account = Account.objects.filter(user=request.user)[0]

    cur_dict = client.get_exchange_rates(currency='ETH')['rates']
    cur_dict = {k: cur_dict[k] for k in ('USD','BTC') if k in cur_dict}
    render_di['price'] = cur_dict['USD']

    render_di['bal'] = client.get_account(account.account_id).balance.amount
    render_di['address'] = client.create_address(account.account_id).address

    return render(request, 'account.html', render_di)
