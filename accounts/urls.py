from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.account_view, name='account_view'),
    url(r'^send/', views.send_view, name='send_view'),
    url(r'^redeem/', views.redeem_view, name='redeem_view'),
]
