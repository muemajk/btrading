from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Register your models here.
from .models import Client, ClientSession ,Employee

class EmployeeInline(admin.StackedInline):
    model = Employee
    can_delete = False
    verbose_name_plural = 'Employee'


class UserAdmin(BaseUserAdmin):
    inlines = (EmployeeInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Client)
admin.site.register(ClientSession)