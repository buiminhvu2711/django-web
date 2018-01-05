from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['sanpham',]

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'hoten', 'email', 
                    'diachi', 'hinhthucthanhtoan','thanhtoan',
                    'get_datetime', 'get_datetime2',] #_display hien thi len man hinh
    list_filter = ['thanhtoan', 'ngaytao', 'ngaycapnhat'] #_filter chuc nang sap xep
    inlines = [OrderItemInline]
    
admin.site.register(Order, OrderAdmin)