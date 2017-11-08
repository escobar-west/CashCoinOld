from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Account
from coinbase.wallet.client import Client

client = Client(
        '3tFVaskD7hLfA2b8',
        'UFzzkgpLYSTIBYFTSgXvPaXt9KqcNKi8',
        api_version='2017-10-29',)

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

def send_view(request):
    if request.method == 'POST':
        account = Account.objects.filter(user=request.user)[0]
        address = request.POST['address']
        amount = float(request.POST['amount'])
        print(account.account_id)
        tx = client.send_money(account.account_id,
                               to=address,
                               amount=amount,
                               currency='BTC')
    
        return HttpResponse(tx)
    else:
        return HttpResponse('not a post')
def redeem_view(request):
    render_di = {}
    if request.method == 'POST':
        import sys
        sys.path.append('/Users/escobar/cashcoin/')
        from coupons.models import Coupon

        entered_key = request.POST['key_val']
        coupon_list = Coupon.objects.filter(key_val=entered_key)

        if len(coupon_list) == 1:
            import requests
            account = Account.objects.filter(user=request.user)[0]
            url = 'https://api.kraken.com/0/public/Ticker?pair=XBTUSD'
            r = requests.get(url)
            btc_price = float(r.json()['result']['XXBTZUSD']['c'][0])
            btc_amt = coupon_list[0].value / btc_price
            tx = client.transfer_money('03609ae5-9310-58b7-be2e-4754fae12e14',
                                       to=account.account_id,
                                       amount=0.001,
                                       currency='BTC'
                                      )
            print(tx)
            return HttpResponse('The coupon value is {} and the btc price is {} and {}'.format(
                                                    coupon_list[0].value,
                                                    btc_amt,
                                                    tx))
        else:
            render_di['post_error'] = True
    else:
        render_di['post_error'] = False

    return render(request, 'redeem.html', render_di)





