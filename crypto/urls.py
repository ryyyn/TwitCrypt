from django.conf.urls import url
from . import views

app_name = "crypto"

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^encrypt/', views.encrypt, name='encrypt'),
    url(r'^decrypt/', views.decrypt, name='decrypt'),
]

# ignore these comments:
#    might need replacement elsewhere for 'app_name=' to resolve namespace??
#    refactor as crypto/urls.py if necessary
