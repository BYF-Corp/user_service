from django.contrib import admin
from user_management.models import Customer, Employee


# Register your models here.
admin.site.register(Customer)
admin.site.register(Employee)