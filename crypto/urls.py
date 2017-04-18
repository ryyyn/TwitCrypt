from django.conf.urls import url
from . import views

app_name = "crypto"

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^encrypt/', views.encrypt, name='encrypt'),
    url(r'^decrypt/', views.decrypt, name='decrypt'),
]

