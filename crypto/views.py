from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from crypto.forms import CodeRecordForm, ValidateForm
from crypto.models import CodeRecord

import encryption


def disp_message(request):
    return render(request, 'crypto/message.html')


def home(request):
    return render(request, 'crypto/index.html')


def encrypt(request):
    if request.method == 'POST':
        # create form instance and populate it with request data
        form = CodeRecordForm(data=request.POST)
        if form.is_valid():
            message = form.cleaned_data['code']
            # exp_time = form.cleaned_data['exp_time']
            otp = encryption.gen_otp()
            code = encryption.encrypt(message, otp)
            CodeRecord.objects.create(code=code, otp=otp,
                                      password=form.cleaned_data['password']
                                      )
            context = {
                'intro_text': "<p>Your secret message. Anyone with the password can decrypt it.</p>",
                'message': code,
            }
            return render(
                request,
                'crypto/message.html',
                context
            )
    else:
        form = CodeRecordForm()

    return render(request, 'crypto/encrypt.html', {'form': form})


def decrypt(request):
    if request.method == 'POST':
        # create form instance and populate it with request data
        form = ValidateForm(data=request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            try:
                code_rec = CodeRecord.objects.get(code=code,
                                                  password=form.cleaned_data['password']
                                                  )
            except ObjectDoesNotExist:
                print("No record found")
                return HttpResponseRedirect('crypto.decrypt.html')
            else:
                context = {
                    'intro_text': "<p>Decrypted message:</p>",
                    'message': encryption.decrypt(code, code_rec.otp),
                }
                return render(
                        request,
                        'crypto/message.html',
                        context,
                )
    else:
        form = ValidateForm()

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