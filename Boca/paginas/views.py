from multiprocessing import context
from re import template
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views.generic.detail import DetailView

from .models import contest
from .forms import contestForm, optionForm
# Create your views here.
def index(request):
    template = loader.get_template('home/index.html')
    context = {}
    return HttpResponse(template.render(context,request))

def administrador(request):
    template = loader.get_template('otros/administrator.html')
    context = {}
    return HttpResponse(template.render(context,request))

def contestv(request):
    lista = contest.objects.all()
    context = {'lista':lista}
    template = loader.get_template('otros/contest.html')
    return HttpResponse(template.render(context,request))

def new_contest(request):

    context = {}

    form = contestForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('new_contest')
    
    context['form'] = form
    return render(request,'otros/new_contest.html', context)

def option(request):

    context = {}

    form = optionForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('option')
    
    context['form'] = form
    return render(request,'otros/option.html', context)