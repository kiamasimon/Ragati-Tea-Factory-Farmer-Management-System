from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Farmer(get_user_model()):
    location = models.CharField(max_length=200, blank=True, null=True)
    phone_number = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name = 'Farmer'


class Employee(get_user_model()):
    class Meta:
        verbose_name = 'Employee'


class Sale(models.Model):
    farmer_id = models.ForeignKey(Farmer, related_name='farmer',unique=False, blank=True, null=True,
                                  on_delete=models.CASCADE)
    kg_of_tea = models.IntegerField(unique=False)
    unit_cost = models.IntegerField(unique=False)
    total = models.IntegerField(unique=False)
    employee_id = models.ForeignKey(Employee, unique=False, related_name='employee', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Sale'

    def year(self):
        return self.created_at.year()


class Tea(models.Model):
    BP1 = 1
    PF1 = 2
    PDUST = 3
    DUST1 = 4

    ANSWER_TYPE_CHOICES = (
        (BP1, 'BP1'),
        (PF1, 'PF1'),
        (PDUST, 'PDUST'),
        (DUST1, 'DUST1'),
    )

    tea_type = models.IntegerField(choices=ANSWER_TYPE_CHOICES, default=BP1, blank=False, null=False)
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    employee = models.ForeignKey(Employee, related_name='employee_name', on_delete=models.CASCADE)

