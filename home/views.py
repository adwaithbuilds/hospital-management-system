from django.shortcuts import render
from django.http import HttpResponse
from.forms import bookingform

from .models import departments, doctors as doctor
# Create your views here.
def index(request):

   return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def booking(request):
    if request.method == "POST":
        form = bookingform(request.POST)
        if form.is_valid():
             form.save()
             return render(request,'confirmation.html')
        
    form = bookingform()
    dict_form={
        'form':form
     }
    return render(request, 'booking.html',dict_form)
 
def doctors(request):
    dict_docs ={
        'doctors': doctor.objects.all()
    }
    return render(request, 'doctors.html',dict_docs)

def department(request):
    dict_dept={
        'dept':departments.objects.all() 
    }
    return render(request, 'department.html',dict_dept)

def contacts(request):
   
    return render(request, 'contacts.html')