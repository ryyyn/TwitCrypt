from django.conf.urls import url
from . import views

app_name = "crypto"

urlpatterns = [
    url(r'^$', views.home, name='crypto-home'),
    url(r'^encrypt/', views.encrypt, name='crypto-encrypt'),
    url(r'^decrypt/', views.decrypt, name='crypto-decrypt'),
    url(r'^message/', views.get_message, name='crypto-message'),
]

