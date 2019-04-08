from django.contrib.auth import authenticate, logout, login, get_user_model
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from accounts.forms import SignUpForm
from accounts.models import Farmer, Employee


def user_login(request):
    msg = []

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                if Farmer.objects.filter(user_ptr_id=user.id).exists():
                    return redirect('Farmer:my_sales')
                if Employee.objects.filter(user_ptr_id=user.id).exists():
                    return redirect('Employee:dashboard')
            else:
                msg.append('You account has been deactivated!')
    else:
        msg.append('Invalid login')
    return render(request, 'accounts/login.html', {'errors': msg})


def logout_view(request):
    logout(request)
    return redirect('QED:landingpage')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        print(form)
        # pdb.set_trace()
        if form.is_valid():
            farmer = form.save(commit=False)
            farmer.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})


def dashboard(request):
    return render(request, 'accounts/home.html')