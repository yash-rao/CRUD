from django.shortcuts import redirect, render,HttpResponseRedirect
from .forms import Studentform
from .models import User
# Create your views here.
def add_show(request):
    if request.method == 'POST':
        S_form = Studentform(request.POST)
 #       if S_form.is_valid():  shortcut
 #           S_form.save()      shortcut without clean
        if S_form.is_valid():
            n=S_form.cleaned_data['name']
            e=S_form.cleaned_data['email']
            p=S_form.cleaned_data['password']
            reg=User(name=n,email=e,password=p)
            reg.save()
    else:
        S_form = Studentform()
    s=User.objects.all()
    return render(request,'register/in_out.html',{'form':S_form,'student':s})

def delete_data(request, id):
    if request.method == 'POST':
        ob=User.objects.get(pk=id)
        ob.delete()
        return HttpResponseRedirect('/')

def update_stud(request, id):
    if request.method == 'POST':
        new=User.objects.get(pk=id)
        S_form=Studentform(request.POST,instance=new)
        if S_form.is_valid():
            S_form.save()
            return redirect('http://127.0.0.1:8000/')
    else:
        new=User.objects.get(pk=id)
        S_form=Studentform(instance=new)
    return render(request,'register/update.html',{'fm':S_form})