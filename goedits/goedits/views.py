from django.http import HttpResponse
from django.template import loader

def hello(request):
    template = loader.get_template('hello.html')
    context = {
        'data': 'hello mani',
    }
    return HttpResponse(template.render(context, request))
	
	
def login(request):
    template = loader.get_template('login.html')
    context = {
        'data': 'login',
    }
    return HttpResponse(template.render(context, request))	
	
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
        'data': 'compare',
    }
    return HttpResponse(template.render(context, request))
	
def contact(request):
    template = loader.get_template('contact.html')
    context = {
        'data': 'compare',
    }
    return HttpResponse(template.render(context, request))
	
