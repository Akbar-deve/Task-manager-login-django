from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.hashers import make_password
from .models import NUser, Todo
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.http import JsonResponse
from django.contrib import  auth
# from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views import View
from datetime import datetime
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


# ....Admin section .........
def admin_signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email_id']
        password = request.POST['password']
        is_staff = request.POST.get('is_staff', False) #form is_staff checked then it will return on
        is_staff = is_staff == "on"  # result will be true / false
       
        is_superuser = request.POST.get('is_superuser', False)
        is_superuser = is_superuser == 'on' # result will be true / false

        x = User.objects.create_user(username=username, password=password, email=email, is_superuser=is_superuser, is_staff=is_staff)
        x.save()
        return redirect('admin_login')

    all_users = User.objects.all()
    return render(request, 'admin_signup.html', {'all_users': all_users})

def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        u = auth.authenticate(request, username=username, password=password)
        print("user-->", u)
        if u is not None:
            print("if user-->", u)
            auth.login(request,u)
            return redirect('admin_dashboard') 
        else:
            print("else user-->", u) 
            return render(request, 'admin_login.html', {'error': 'Invalid username or password.'})

    return render(request, 'admin_login.html')

@login_required(login_url='admin_login')
def admin_dashboard(request):
    
        users = NUser.objects.all()
       
        return render(request, 'admin_dashboard.html', {'users': users})

def update_status(request):
    if request.method == 'POST':
        user_id = request.POST.get('userId')
        new_status = request.POST.get('newStatus')

        try:
            user = NUser.objects.get(pk=user_id)
            user.status = new_status
            user.save()
            return redirect('admin_dashboard')
        except NUser.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)

    return JsonResponse({'error': 'Invalid request'}, status=400)

def admin_logout(request):
    auth.logout(request)
    return redirect('admin_login')
# ......... Admin section Ends............



# .......User Section .............
# from .backends import CustomUserBackend

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        status = request.POST['status']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        print(username, password, email)
        if password == confirm_password:
            x = User.objects.create_user(username=username, password=password, email=email, is_superuser="False", is_staff="True")
            x.save()
            password = make_password(password) 
            user = NUser(username=username, email=email, password=password, status=status, confirm_password=confirm_password)
            user.save()
            return redirect('Nlogin')
        else:
            return render(request, 'signup.html', {"error": 'Password does not match with the confirm password'})

    return render(request, 'signup.html')

# def Nlogin(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
        
       
#         user = authenticate(request, username=username, password=password)
#         print('main user -->',user)
#         if user is not None:
#             print('if user -->',user)
#             login(request, user)
#             print('if-1 user -->',user)
#             return redirect('home')  
#         else:
#             print("else user->",user)
#             return render(request, 'login.html', {'error': 'Invalid username or password.'})
    
   
#     return render(request, 'login.html')

import bcrypt



def Nlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            user = NUser.objects.get(username=username)
            u = auth.authenticate(request, username=username, password=password)
            print("user-->",user)
            if user.status == "enable":
                # Password matches, log the user in
                print("password->",password)
                auth.login(request,u)
                return redirect('home')
            else:
                return render(request, 'login.html', {'error': 'User not Enabled.'})
        except NUser.DoesNotExist:
            # User does not exist
            return render(request, 'login.html', {'error': 'Invalid username or password'})

    return render(request, 'login.html')

# .........................................
# @login_required(login_url='Nlogin')
# def home(request):
#     tasks = Todo.objects.all()
#     u = NUser.objects.all()
#     print("get home")
#     return render(request, 'home.html', {'tasks': tasks,"u":u})

@login_required(login_url='Nlogin')
def home(request):
    tasks = Todo.objects.all()
    u = NUser.objects.all()
    print("get home")
    return render(request, 'home.html', {'tasks': tasks, "u": u, 'user': request.user})

def Nlogout(request):
    auth.logout(request)
    return redirect('Nlogin') 

# ......User Section ends...........

# ------------------TODO--------------------------------------

class AddTaskView(View):
    template_name = 'add_task.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        title = request.POST['title']
        status = request.POST['status']
        due_date_str = request.POST['due_date']
        due_date = datetime.strptime(due_date_str, '%Y-%m-%dT%H:%M')
        task = Todo(title=title, status = status, due_date=due_date)
       
        task.save()
        return redirect('home')



class UpdateTaskView(View):
    template_name = 'update_task.html'

    def get(self, request, task_id):
        task = get_object_or_404(Todo, pk=task_id)
        return render(request, self.template_name, {'task': task})

    def post(self, request, task_id):
        task = get_object_or_404(Todo, pk=task_id)
        title = request.POST.get('title')
        status = request.POST.get('status')
        due_date_str = request.POST.get('due_date')
        due_date = datetime.strptime(due_date_str, '%Y-%m-%dT%H:%M')


        task.title = title
        task.status = status
        task.due_date = due_date
       
        task.save()
        return redirect('home')


class DeleteTaskView(View):

    def get(self, request, task_id):
        task = get_object_or_404(Todo, pk=task_id)
        return render(request, 'delete_task.html', {'task': task})

    def post(self, request, task_id):
        task = get_object_or_404(Todo, pk=task_id)
        task.delete()
        return redirect('home')