from django.contrib import admin

from accounts.models import Farmer, Employee, Sale, Tea

admin.site.register(Farmer)
admin.site.register(Employee)
admin.site.register(Sale)
admin.site.register(Tea)
