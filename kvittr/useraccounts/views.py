from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User

def user_login(request):
    context = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            # redirect to a success page.
            return redirect('post_listing')
        else:
            # render login again, but display error message
            context['login_failed'] = True
    return render(request, 'useraccounts/login.html', context)

def user_logout(request):
    logout(request)
    return redirect('frontpage')

def user_register(request):
    context = {}
    if request.method == 'POST':
        user = User()
        user.first_name = request.POST.get('firstname')
        user.last_name = request.POST.get('lastname')
        if User.objects.filter(username=request.POST['username']).exists():#Check if username exists in db
            context['username_exist'] = True
        elif User.objects.filter(email=request.POST['email']).exists():#Check if email exists in db
            context['email_exist'] = True
        else:
            user.username = request.POST.get('username')
            user.email = request.POST.get('email')
            user.set_password(request.POST.get('password'))
            user.save()
            context['user_saved_successfully'] = True
    return render(request, 'useraccounts/register.html', context)

def user_edit(request):
    context = {}
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get('firstname')
        user.last_name = request.POST.get('lastname')
        user.email = request.POST.get('email')  
        user.save(update_fields=["first_name", "last_name", "email"]) 
        context['user_edited_successfully'] = True
    return render(request, 'useraccounts/edit.html', context)
        