from django.db import models
from django.db.models import Func, Sum
from django.shortcuts import render
from accounts.models import Sale, Tea


def index(request):
     return render(request, 'farmer/index.html')


#resolve week in a date
class Week(Func):
    function = 'EXTRACT'
    template = '%(function)s(WEEK from %(expressions)s)'
    output_field = models.IntegerField()


#resolve Month in a date
class Month(Func):
    function = 'EXTRACT'
    template = '%(function)s(MONTH from %(expressions)s)'
    output_field = models.IntegerField()


#resolve Year in a date
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
        'sum_up': sum_up
    }
    return render(request, 'farmer/my_sales.html', context)


def tea_prices(request):
    tea = Tea.objects.all()
    tea_prices = tea.annotate(week=Week('created_at')).values('week', 'tea_type', 'price', 'created_at',
                                                              'employee').order_by("week")
    context = {
        'tea_prices': tea_prices
    }
    return render(request, 'farmer/tea_prices.html', context)




