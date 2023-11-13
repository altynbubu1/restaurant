from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


def login(request):
    """
    username
    password
    """

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # print(username, password, sep="\n")

        user = auth.authenticate(
            username=username,
            password=password
        )
        # print(user)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            return redirect('login')
    return render(request, 'accounts/login.html')


def register(request):
    """
    name
    lastname
    email
    username
    password1
    password2
    """
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['first_name']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        # print(first_name, last_name, email, username, password1, password2, sep="\n")
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    return redirect('register')
                else:
                    user = User.objects.create_user(
                        first_name=first_name,
                        last_name=last_name,
                        email=email,
                        username=username,
                        password=password1
                    )

                    user.save()
                    return redirect('index')
        else:
            return redirect('register')

    return render(request, 'accounts/register.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        print('logout')
        return redirect('index')