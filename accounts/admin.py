from django.contrib import admin

from accounts.models import Farmer, Employee, Sale

admin.site.register(Farmer)
admin.site.register(Employee)
admin.site.register(Sale)
