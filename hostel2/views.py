from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


def base(request):
    return render(request, 'hostel2/landingpage.html')



def home(request):
    return render(request, 'hostel2/homenew.html')

def gallery(request):
    return render(request, 'hostel2/gallery.html')
def legend(request):
    return render(request, 'hostel2/gallery.html')
def contactus(request):
    return render(request, 'hostel2/gallery.html')