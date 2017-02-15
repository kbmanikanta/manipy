import os
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages	
from django.conf import settings
from goedits.form import MailForm
import sendgrid
from django.template import loader
from django.core.mail import send_mail, BadHeaderError

def index(request):
    template = loader.get_template('index.html')
    context = {
        'data': 'index',
    }
    return HttpResponse(template.render(context, request))
	
def compare(request):
    template = loader.get_template('compare.html')
    context = {
        'data': 'compare',
    }
    return HttpResponse(template.render(context, request))
	
def pricing(request):
    template = loader.get_template('pricing.html')
    context = {
        'data': 'pricing',
    }
    return HttpResponse(template.render(context, request))
	
def service(request):
    template = loader.get_template('service.html')
    context = {
        'data': 'service',
    }
    return HttpResponse(template.render(context, request))
	
def contact(request):
    if request.method == 'POST':
        form = MailForm(request.POST)
        if form.is_valid():
            to_mail = str(form.cleaned_data['to_mail'])
            cname_mail = str(form.cleaned_data['cname_mail'])
            content_mail = str(form.cleaned_data['content_mail']) + str(form.cleaned_data['mail_subject'])
            sg = sendgrid.SendGridClient(settings.SENDGRID_USERNAME, settings.SENDGRID_PASSWORD)
            message = sendgrid.Mail()
            message.add_to(to_mail)
            message.set_subject(cname_mail)
            message.set_html(content_mail)
            message.set_text(content_mail)
            message.set_from('contact@goedits.com')
            status, msg = sg.send(message)

            if status == 200:
                messages.success(request, 'Your email was successfully sent.')
            else:
                messages.error(request, msg)   
    else:
        form = MailForm()
    return render(request, 'contact.html', {
        'form': form,
    })