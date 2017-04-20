from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from .forms import MessageForm
from .models import Auth



'''
class IndexView(generic.View):
    template_name = 'crypto/index.html'


class DecryptView(generic.DetailView):
    template_name = 'crypto/decrypt.html'


class EncryptView(generic.DetailView):
    template_name = 'crypto/encrypt.html'

'''


def get_message(request):
    if request.method == 'POST':
        # create form instance and populate it with request data
        form = MessageForm(request.POST)

        if form.is_valid():
            # process

            return HttpResponseRedirect('/ok/')

    else:
        form = MessageForm()

    return render(request, 'encrypt.html', {'form': form})


def home(request):
    return render(request, 'crypto/index.html')


def encrypt(request):
    return render(request, 'crypto/encrypt.html')


def decrypt(request):
    return render(request, 'crypto/decrypt.html')
