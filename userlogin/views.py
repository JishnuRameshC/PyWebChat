from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

def demo(request):
    return render(request, "userlogin/demo.html")

def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        email_or_username = request.POST.get('email_or_username').lower()
        password = request.POST.get('password')
        try:
            user = User.objects.get(email=email_or_username)
        except User.DoesNotExist:
            try:
                user = User.objects.get(username=email_or_username)
            except User.DoesNotExist:
                user = None

        if user is not None:
            authenticated_user = authenticate(request, username=user.username, password=password)
        else:
            authenticated_user = None

        if authenticated_user is not None:
            login(request, authenticated_user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid email/username or password')
            return redirect('login')

    context = {'page': page}
    return render(request, 'userlogin/s.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')


def registerPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse('Your password and confirm password are not the same!')

        # Check if the username already exists
        if User.objects.filter(username=uname).exists():
            return HttpResponse('Username already exists. Please choose a different username.')

        # If username is unique, create the user
        my_user = User.objects.create_user(uname, email, pass1)
        my_user.save()
        return redirect('home')
    return render(request, 'userlogin/s.html')





