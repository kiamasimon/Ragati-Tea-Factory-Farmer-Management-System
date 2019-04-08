from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from accounts.models import Farmer, Sale, Employee
from django.contrib import messages

from employee.forms import AddSaleForm, SignUpForm


def list_farmers(request):
    farmers = Farmer.objects.all()

    context = {
        'farmers': farmers
    }

    return render(request, 'employee/farmers_list.html', context)


@staff_member_required
def deactivate_farmer(request, farmer_id):
    farmer = Farmer.objects.get(user_ptr_id=farmer_id)
    farmer.is_active = False
    farmer.save()
    messages.success(request, "Farmer account has been successfully deactivated!")
    return redirect('Employee:list_farmers')


@staff_member_required
def activate_farmer(request, farmer_id):
    farmer = Farmer.objects.get(user_ptr_id=farmer_id)
    farmer.is_active = True
    farmer.save()
    messages.success(request, "Farmer has been successfully activated!")
    return redirect('Employee:list_farmers')


def sales_list(request):
    farmers = Farmer.objects.all()

    context = {
        'farmers': farmers
    }

    return render(request, 'employee/sales_list.html', context)


def farmer_sales(request, pk):
    farmer = Farmer.objects.filter(id=pk)

    sales = Sale.objects.filter(farmer_id=pk)

    context = {
        'sales': sales,
        'farmer': farmer
    }
    return render(request, 'employee/farmer_sales.html', context)


@staff_member_required
def add_sale(request):
    farmers = Farmer.objects.all()
    if request.method == 'POST':
        form = AddSaleForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sale added successfully')
            return redirect('Employee:add_sale')
    else:
            form = AddSaleForm()
    return render(request, 'employee/add_sale.html', {'form': form, 'farmers': farmers})


def admin_signup(request):
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
            return redirect('Employee:dashboard')
    else:
        form = SignUpForm()
    return render(request, 'employee/sign_up.html', {'form': form})


@staff_member_required()
def dashboard(request):
    context = {
        'sales': Sale.objects.count(),
        'farmers': Farmer.objects.count(),
        'employees': Employee.objects.count(),
    }
    return render(request, 'employee/dashboard.html', context)
