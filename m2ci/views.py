from django.shortcuts import render

def index(request):
    return render(request, 'm2ci/index.html')
def Home(request):
    return render(request, 'm2ci/Home.html')

def News(request):
    return render(request, 'm2ci/News.html')

def Portfolio(request):
    return render(request, 'm2ci/Portfolio.html')

def Services(request):
    return render(request, 'm2ci/ourServices.html')

def About(request):
    return render(request, 'm2ci/About.html')

def Team(request):
    return render(request, 'm2ci/Team.html')

def Contact(request):
    return render(request, 'm2ci/Contact.html')
