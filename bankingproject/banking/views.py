# Create your views here.
from django.contrib import messages, auth
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import District, Branch,Person



# Create your views here.
def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        user_name = request.POST['username']
        password = request.POST['password']
        conf_password = request.POST['password1']

        if password == conf_password:
            if User.objects.filter(username=user_name).exists():
                messages.info(request, 'Username Already Taken')
                return redirect('banking:register')

            else:
                user = User.objects.create_user(
                    username=user_name,password=password
                )
                user.save()
                messages.info(request, 'Welcome')
        else:
            messages.info(request, 'Password not matched')
            return redirect('banking:register')

        return redirect('banking:login')

    return render(request, 'register.html')


def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('banking:blank')
        else:
            messages.info(request, 'Invalid Credential')
            return redirect('banking:login')
    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def blank(request):
    return render(request, 'blank.html')


def add(request):
    if request.method == 'POST':
        name = request.POST['name']
        dob = request.POST['dob']
        age = request.POST['age']
        gender = request.POST['gender']
        phone = request.POST['phone']
        email = request.POST['email']
        address = request.POST['address']
        district = request.POST['district']
        district = District.objects.get(id=district)
        branch = request.POST['branch']
        branch = Branch.objects.get(id=branch)
        account = request.POST['account']
        material = request.POST.getlist('material[]')
        person = Person(
            name=name,
            dob=dob,
            age=age,
            gender=gender,
            phone=phone,
            email=email,
            address=address,
            district=district,
            branch=branch,
            account=account,
            material=material
        )
        person.save()
        messages.info(request, 'Application Accepted')

    dist = District.objects.all()
    bran = Branch.objects.all()
    return render(request, 'add.html', {'dist': dist, 'bran': bran, })


