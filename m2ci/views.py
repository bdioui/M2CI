from django.shortcuts import render
from .forms import message_form
from django.core.mail import send_mail
from django.conf import settings

def index(request):
    return render(request, 'm2ci/index.html')
def Home(request):
    context = {}
    if request.method == "POST":
        form = message_form(request.POST)
        if form.is_valid():
            form.save()
            full_name = form.cleaned_data.get('full_name')
            context['full_name'] = full_name
            email = form.cleaned_data.get('email')
            sujet = form.cleaned_data.get('sujet')
            message = form.cleaned_data.get('message')
            to = 'bdiouipierre@gmail.com'

            subject = "Nouveau message sur votre application !"
            message = 'de :'+ email + '| message : ' + message
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [to]

            send_mail(subject, message, email_from, recipient_list)
            return render(request, 'm2ci/message_reçu.html', context)
        else:
            form = message_form()
            context['form'] = form
            return render(request, 'm2ci/Home.html')
    else:
        form = message_form(request.POST)
        context['form'] = form
        return render(request, 'm2ci/Home.html')

def News(request):
    return render(request, 'm2ci/News.html')

def Portfolio(request):
    return render(request, 'm2ci/Portfolio.html')

def Services(request):
    context = {}
    if request.method == "POST":
        form = message_form(request.POST)
        if form.is_valid():
            form.save()
            full_name = form.cleaned_data.get('full_name')
            context['full_name'] = full_name
            email = form.cleaned_data.get('email')
            sujet = form.cleaned_data.get('sujet')
            message = form.cleaned_data.get('message')
            to = 'bdiouipierre@gmail.com'

            subject = 'Nouveau message sur vore application !'
            message = 'de :'+ email + '| message : ' + message
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [to]

            send_mail(subject, message, email_from, recipient_list)
            return render(request, 'm2ci/message_reçu.html', context)
        else:
            form = message_form()
            context['form'] = form
            return render(request, 'm2ci/ourServices.html')
    else:
        form = message_form(request.POST)
        context['form'] = form
        return render(request, 'm2ci/ourServices.html')

def About(request):
    return render(request, 'm2ci/About.html')

def Team(request):
    return render(request, 'm2ci/Team.html')

def Contact(request):
    context = {}
    if request.method == "POST":
        form = message_form(request.POST)
        if form.is_valid():
            form.save()
            full_name = form.cleaned_data.get('full_name')
            email = form.cleaned_data.get('email')
            sujet = form.cleaned_data.get('sujet')
            message = form.cleaned_data.get('message')
            to = 'bdiouipierre@gmail.com'

            subject = 'Nouveau message sur votre application !'
            message = 'de :'+ email + '| message : ' + message
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [to]

            send_mail(subject, message, email_from, recipient_list)

            context['full_name'] = full_name
            return render(request, 'm2ci/message_reçu.html', context)
        else:
            form = message_form()
            context['form'] = form
            return render(request, 'm2ci/Contact.html', context)
    else:
        form = message_form(request.POST)
        context['form'] = form
        return render(request, 'm2ci/Contact.html', context)
