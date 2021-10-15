from django.contrib import admin
from .models import Product, Comments, Employee, Message

admin.site.register(Product)
admin.site.register(Comments)
admin.site.register(Employee)
admin.site.register(Message)

# Register your models here.
