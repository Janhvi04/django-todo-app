from  django . shortcuts  import  render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from todo import models
from todo.models import TODOO
from django.contrib.auth.decorators import login_required



@login_required(login_url='/loginn')
def home(request):
    return redirect('/todopage')


def signup(request):
    if request.method == 'POST':
        fnm=request.POST.get('fnm')
        emailid=request.POST.get('emailid')
        pwd=request.POST.get('pwd')
        print(fnm,emailid,pwd)
        
        # Validate input fields
        if not fnm or not emailid or not pwd:
            messages.error(request, 'All fields are required.')
            return render(request, 'signup.html')
        
        # Check if username already exists
        if User.objects.filter(username=fnm).exists():
            messages.error(request, 'Username already exists. Please choose a different username.')
            return render(request, 'signup.html')
        
        # Check if email already exists
        if User.objects.filter(email=emailid).exists():
            messages.error(request, 'Email already registered. Please use a different email or login.')
            return render(request, 'signup.html')
        
        try:
            # Create user - create_user() automatically saves to database
            my_user = User.objects.create_user(username=fnm, email=emailid, password=pwd)
            # Explicitly save to ensure it's committed to database
            my_user.save()
            print(f"User created successfully: {my_user.username}, ID: {my_user.id}")
            messages.success(request, 'Account created successfully! Please login.')
            return redirect('/loginn')
        except Exception as e:
            print(f"Error creating user: {str(e)}")
            messages.error(request, f'Error creating account: {str(e)}')
            return render(request, 'signup.html')
    
    return render(request, 'signup.html')
        
     
        
        
        
        
    

def loginn(request):
    if request.method == 'POST':
        fnm=request.POST.get('fnm')
        pwd=request.POST.get('pwd')
        print(fnm,pwd)
        userr=authenticate(request,username=fnm,password=pwd)
        if userr is not None:
            login(request,userr)
            messages.success(request, f'Welcome back, {fnm}!')
            return redirect('/todopage')
        else:
            messages.error(request, 'Invalid username or password. Please try again.')
            return render(request, 'loginn.html')
               
    return render(request, 'loginn.html')
        
@login_required(login_url='/loginn')
def todo(request):
    if request.method == 'POST':
        title=request.POST.get('title')
        print(title)
        obj=models.TODOO(title=title,user=request.user)
        obj.save()
        return redirect('/todopage')
        
    # Order by completed status (incomplete first), then by date (newest first)
    res=models.TODOO.objects.filter(user=request.user).order_by('completed', '-data')
    return render(request, 'todo.html',{'res':res,})

@login_required(login_url='/loginn')
def delete_todo(request,srno):
    print(srno)
    obj=models.TODOO.objects.get(srno=srno, user=request.user)
    obj.delete()
    return redirect('/todopage')

@login_required(login_url='/loginn')
def edit_todo(request, srno):
    obj = models.TODOO.objects.get(srno=srno, user=request.user)
    if request.method == 'POST':
        title = request.POST.get('title')
        print(title)
        obj.title = title
        obj.save()
        return redirect('/todopage')

    return render(request, 'edit_todo.html', {'obj': obj})

@login_required(login_url='/loginn')
def toggle_complete(request, srno):
    obj = models.TODOO.objects.get(srno=srno, user=request.user)
    obj.completed = not obj.completed
    obj.save()
    return redirect('/todopage')





def signout(request):
    logout(request)
    return redirect('/loginn')
