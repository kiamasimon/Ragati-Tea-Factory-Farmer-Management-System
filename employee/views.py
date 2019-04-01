from django.shortcuts import render, redirect
from accounts.models import Farmer, Sale
from django.contrib import messages


def dashboard(request):
    return render(request, 'employee/dashboard.html')


def list_farmers(request):
    farmers = Farmer.objects.all()

    context = {
        'farmers': farmers
    }

    return render(request, 'employee/farmers_list.html', context)


def deactivate_farmer(request, farmer_id):
    farmer = Farmer.objects.get(user_ptr_id=farmer_id)
    farmer.is_active = False
    farmer.save()
    messages.success(request, "Farmer account has been successfully deactivated!")
    return redirect('Employee:list_farmers')


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
    return  render(request, 'employee/farmer_sales.html', context)