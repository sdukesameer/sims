from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db.models import Count
from .forms import MyForm
from .models import myform
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def prof(request,pk):
    task = myform.objects.get(id=pk)
    # form = MyForm(instance=task)
    # fn = myform.objects.get(user=request.user)
    return render(request,'views.html',{'task':task})

def loginPage(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('main')
		else:
			messages.info(request, 'Username OR password is incorrect')
			return render(request, 'login.html', {})
	return render(request, 'login.html', {})

@login_required(login_url='login')
def logoutUser(request):
	logout(request)
	return redirect('login')

@login_required(login_url='login')
def formr(request):
    form=MyForm()
    if request.method == 'POST':
        form = MyForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/view')
    return render(request,'addstudent.html',{'form':form})


@login_required(login_url='login')
def viewdata(request):
    data=myform.objects.all()
    return render(request,'view.html',{'data':data})


@login_required(login_url='login')
def UpdateTask(request,pk):
    task = myform.objects.get(id=pk)
    form = MyForm(instance=task)
    if request.method == 'POST':
        form = MyForm(request.POST,request.FILES,instance=task)
        if form.is_valid():
            form.save()
            return redirect('/view')



    return render(request,'update.html',{'form':form})


@login_required(login_url='login')
def DeleteTask(request,pk):
    item = myform.objects.get(id=pk)
    
    if request.method == 'POST':
        item.delete()
        return redirect('/view')

    return render(request,'delete.html',{'item':item})

@login_required(login_url='login')
def mainarea(request):
    item=myform.objects.all()
    BTech=myform.objects.filter(Course='B.Tech').count()
    BCA=myform.objects.filter(Course='BCA').count()
    BBA=myform.objects.filter(Course='BBA').count()
    Masters=myform.objects.filter(Course='Masters').count()
    mydict={'item':item,'BTech':BTech,'BCA':BCA,'BBA':BBA,'Masters':Masters}
    return render(request,'mainarea.html',mydict)

    

    
        
    

