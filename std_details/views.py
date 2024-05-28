from django.shortcuts import render, HttpResponseRedirect, redirect
from .forms import StudentReg
from .models import Student
# Create your views here.


# Create
def std_list(request):
    if request.method == 'POST':
        fm = StudentReg(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            address = fm.cleaned_data['address']
            faculty = fm.cleaned_data['faculty']
            reg = Student(name=name, address=address, faculty=faculty)
            reg.save() 
            return redirect('/')   # it will help to blank the field after adding the data

            # if fm.is_valid():
            # fm.save() is short method used to save all the data of fields in database

        #  fm.cleaned_data and reg is used to filtrate the value of fields
            #  no need to write fields whose value you don't want to save like password 

    else:
      return redirect('/') 

    stud = Student.objects.all()    # to retrieve all data from database

    return render (request,'std_list.html', {'form': fm, 'stu':stud})


# Delete
def std_delete(request, id):
    delt = Student.objects.get(id=id)
    delt.delete()
    return HttpResponseRedirect('/')
    


# Update   
def std_edit(request, id):
    if request.method == 'POST':
        id = Student.objects.get(id=id)
        fm = StudentReg(request.POST, instance=id)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            address = fm.cleaned_data['address']
            faculty = fm.cleaned_data['faculty']
            reg = Student (name=name, address=address, faculty=faculty)
            reg.save()
            fm = StudentReg()
    else:
        fm = StudentReg()
        id = Student.objects.get()
        fm= StudentReg(instance=id)
    return render (request, 'std_edit.html', {'form': fm})
    


