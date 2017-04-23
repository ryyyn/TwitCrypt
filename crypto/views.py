from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# from django.contrib.auth import authenticate
# from django.contrib.auth.forms import AuthenticationForm
from crypto.models import CodeRecord

from crypto.forms import CodeRecordForm

import encryption


def disp_message(request):
    return render(request, 'crypto/message.html')


def home(request):
    return render(request, 'crypto/index.html')


def encrypt(request):
    if request.method == 'POST':
        # create form instance and populate it with request data
        form = CodeRecordForm(request.POST)

        if form.is_valid():
            # process
            message = form.cleaned_data['code']
            # exp_time = form.cleaned_data['exp_time']
            otp = encryption.gen_otp()
            code = encryption.encrypt(message, otp)
            print(message, code)
            CodeRecord.objects.create(code=code, otp=otp,
                                      password=form.cleaned_data['password']
                                      )

            return HttpResponseRedirect('/message/') # pass encoded text

    else:
        form = CodeRecordForm()

    return render(request, 'crypto/encrypt.html', {'form': form})


def decrypt(request):
    if request.method == 'POST':
        # create form instance and populate it with request data
        form = CodeRecordForm()

        if form.is_valid():

            validate = False
            CodeRecord.objects.get(code=form.cleaned_data['code'],
                                   password=form.cleaned_data['password']
                                   )


            if validate is not None:
                return HttpResponseRedirect('/message/')

            else:
                return HttpResponseRedirect('/encrypt/')
    else:
        form = CodeRecordForm()

    return render(request, 'crypto/decrypt.html', {'form': form})


'''
# Template based views (implement later if necessary)
class IndexView(generic.View):
    template_name = 'crypto/index.html'


class DecryptView(generic.DetailView):
    template_name = 'crypto/decrypt.html'


class EncryptView(generic.DetailView):
    template_name = 'crypto/encrypt.html'
'''