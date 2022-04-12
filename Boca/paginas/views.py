from multiprocessing import context
from re import template
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views.generic.detail import DetailView

from .forms import contestForm, optionForm
# Create your views here.
def index(request):
    template = loader.get_template('home/index.html')
    context = {}
    return HttpResponse(template.render(context,request))

def contest(request):
    template = loader.get_template('otros/contest.html')
    context = {}
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
    
    context['form'] = form
    return render(request,'otros/option.html', context)