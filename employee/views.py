from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Sum, Count
from django.http import HttpResponse
from django.shortcuts import render, redirect
from accounts.models import Farmer, Sale, Employee, Tea
from django.contrib import messages

from employee.forms import AddSaleForm, SignUpForm, ChangeTeaPricesForm
from farmer.views import Week, Month


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
    print(Sale.objects.filter(farmer_id=pk).aggregate(Sum('total')))
    context = {
        'sales': sales,
        'farmer': farmer,
        'total_sum': Sale.objects.filter(farmer_id=pk).aggregate(Sum('total'))
    }
    return render(request, 'employee/farmer_sales.html', context)


@staff_member_required
def add_sale(request):
    farmers = Farmer.objects.all()
    user = request.user
    employee = Employee.objects.get(user_ptr_id=user.id)

    if request.method == 'POST':
        form = AddSaleForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sale added successfully')
            return redirect('Employee:add_sale')
        else:
            return HttpResponse('Validation error')
    else:
            form = AddSaleForm()
    return render(request, 'employee/add_sale.html', {'form': form, 'farmers': farmers, 'employee': employee, 'user': user})


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


def add_employee(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        print(form)
        # pdb.set_trace()
        if form.is_valid():
            farmer = form.save(commit=False)
            farmer.save()
            messages.success(request, 'Employee Added Successfully')
            return redirect('Employee:manage_employees')
    else:
        form = SignUpForm()
    return render(request, 'employee/add_employee.html', {'form': form})


@staff_member_required()
def dashboard(request):
    sales_list = Sale.objects.all()
    s = sales_list.annotate(month=Month('created_at')).values('month').annotate(monthly_sales=Count('id')).order_by('month')
    print(s)
    context = {
        'sales': Sale.objects.count(),
        'farmers': Farmer.objects.count(),
        'employees': Employee.objects.count(),
        's': s,
    }
    return render(request, 'employee/dashboard.html', context)


def tea_prices(request):
    tea = Tea.objects.all()
    users = User.objects.all()
    tea_prices = tea.annotate(week=Week('created_at')).values('week', 'tea_type', 'price', 'created_at', 'employee','id').order_by("week")
    context = {
        'tea_prices': tea_prices,
        'users': users,
        'tea': tea

    }
    return render(request, 'employee/tea_prices.html', context)


def add_tea_pricing(request):
    tea = Tea.objects.all()
    user = request.user
    employee = Employee.objects.get(user_ptr_id=user.id)

    if request.method == 'POST':
        form = ChangeTeaPricesForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tea Price changed successfully')
            return redirect('Employee:add_tea_pricing')
    else:
        form = ChangeTeaPricesForm()
    return render(request, 'employee/add_tea_pricing.html', {'form': form, 'tea': tea, 'user': user, 'employee': employee})


def edit_tea_pricing(request, tea_type_id):
    tea_instance = Tea.objects.get(id=tea_type_id)
    form = ChangeTeaPricesForm(request.POST, instance=tea_instance)
    tea = Tea.objects.all()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Price Updated Successfully')
            return redirect('Employee:tea_prices')
        else:
            return HttpResponse('Form Invalid')
    else:
        form = ChangeTeaPricesForm()
        return render(request, 'employee/edit_tea_pricing.html', {'form':form, 'tea_instance': tea_instance,'tea': tea})


def profile(request):
    user = request.user
    employee = Employee.objects.filter(user_ptr_id=user.id)

    context = {
        'employee': employee
    }
    return render(request, 'employee/profile.html', context)


def edit_profile(request, user_id):
    employee = Employee.objects.get(user_ptr_id=user_id)
    form = SignUpForm(request.POST, instance=employee)
    users = User.objects.all()

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile Updated Successfully')
            return redirect('Accounts:login')
    return render(request, 'employee/edit_profile.html', {'users': users,'employee': employee})


def manage_employees(request):
    employees = Employee.objects.all()
    list_employees = []
    for employee in employees:
        users = User.objects.filter(id=employee.user_ptr_id)
        list_employees.append(users)
    return render(request, 'employee/manage_employees.html',{'list_employees': list_employees })


@login_required
def deactivate_employee(request, employee_id):
    employee = Employee.objects.get(user_ptr_id=employee_id)
    employee.is_active = False
    employee.save()
    messages.success(request, "Employee account has been successfully deactivated!")
    return redirect('Employee:manage_employees')


@login_required
def activate_employee(request, employee_id):
    employee = Employee.objects.get(user_ptr_id=employee_id)
    employee.is_active = True
    employee.save()
    messages.success(request, "Employee account has been successfully activated!")
    return redirect('Employee:manage_employees')

