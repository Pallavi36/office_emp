from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Department,Role,Employee
from django.db.models import Q

   
def show(request):
    return render(request,'index.html')

def all_emp(request):
    emps=Employee.objects.all()
    return render(request,'all_emp.html',{'emps':emps})

def add_emp(request):
    if request.method=="POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        dept=request.POST['dept']
        salary=int(request.POST['salary'])
        bonus=int(request.POST['bonus'])
        role=request.POST['role']
        phone=int(request.POST['phone'])
        em=Employee(first_name=first_name,last_name=last_name,salary=salary,dept_id=dept,role_id=role,phone=phone,bonus=bonus,hire_date=datetime.now())
        em.save()
        return HttpResponse('Employee Added Successfully')
    elif request.method=="GET":
        return render(request,'add_emp.html')
    else:
        return HttpResponse('Employee has not been added')
def delete_emp(request,emp_id=0):
    if emp_id:
        try:
            emp_to_be_removed=Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
        except:
            return HttpResponse('Please enter a valid empid')
            
    emps=Employee.objects.all()
    return render(request,'delete_emp.html',{'emps':emps})


def filter_emp(request):
    if request.method=="POST":
        name=request.POST['name']
        dept=request.POST['dept']
        role=request.POST['role']
        emps=Employee.objects.all()
        if name:
            emps=emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains  =name))
        if dept:
            emps=emps.filter(dept__name__contains = dept)
        if role:
            emps=emps.filter(role__name__contains = role)
            
        return render(request,'all_emp.html',{'emps':emps})
    elif request.method=='GET':
        return render(request,'filter_emp.html')
    else:
        return HttpResponse('An exception occured')
    return render(request,'filter_emp.html')
    


