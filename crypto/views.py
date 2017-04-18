from django.shortcuts import render

from django.http import HttpResponse
from django.views import generic
from .models import Auth

'''
class IndexView(generic.View):
    template_name = 'crypto/index.html'


class DecryptView(generic.DetailView):
    template_name = 'crypto/decrypt.html'


class EncryptView(generic.DetailView):
    template_name = 'crypto/encrypt.html'

'''

def home(request):
    return render(request, 'crypto/index.html')


def encrypt(request):
    return render(request, 'crypto/encrypt.html')


def decrypt(request):
    return render(request, 'crypto/decrypt.html')
