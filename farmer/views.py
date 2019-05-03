from django.contrib.auth.models import User
from django.db import models
from django.db.models import Func, Sum
from django.http import HttpResponse
from django.shortcuts import render
from accounts.models import Sale, Tea, Employee
from employee.utils import render_to_pdf


def index(request):
     return render(request, 'farmer/index.html')


# resolve week in a date
class Week(Func):
    function = 'EXTRACT'
    template = '%(function)s(WEEK from %(expressions)s)'
    output_field = models.IntegerField()


# resolve Month in a date
class Month(Func):
    function = 'EXTRACT'
    template = '%(function)s(MONTH from %(expressions)s)'
    output_field = models.IntegerField()


# resolve Year in a date
class Year(Func):
    function = 'EXTRACT'
    template = '%(function)s(YEAR from %(expressions)s)'
    output_field = models.IntegerField()


def individual_sales(request):
    user = request.user
    sale = Sale.objects.filter(farmer_id=user.id)

    sales = sale.annotate(week=Week('created_at')).values('week', 'kg_of_tea', 'unit_cost', 'created_at').annotate(total=Sum('total')).order_by("week")
    sum_up = sale.annotate(week=Week('created_at')).values('week').annotate(total=Sum('total')).order_by("week")
    print(sales)
    print(sum_up)

    context = {
        'sales': sales,
        'sum_up': sum_up,
    }

    if request.method == 'POST':
        pdf = render_to_pdf('farmer/my_sales.html')
        return HttpResponse(pdf, content_type='application/pdf')
    else:
        return render(request, 'farmer/my_sales.html', context)


def tea_prices(request):
    tea = Tea.objects.all()
    e = []
    for t in tea:
        employee = Employee.objects.get(user_ptr_id=t.employee)
        user = User.objects.filter(id=employee.user_ptr_id)
        e.append(user)
    tea_prices = tea.annotate(week=Week('created_at')).values('week', 'tea_type', 'price', 'created_at',
                                                              'employee').order_by("week")
    context = {
        'tea_prices': tea_prices,
        'e': e,
    }
    return render(request, 'farmer/tea_prices.html', context)




