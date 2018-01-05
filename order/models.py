from django.db import models
from blog.models import Blog
from datetime import date, datetime

class Order(models.Model):
    hoten = models.CharField(max_length=150)
    email = models.EmailField()
    diachi = models.CharField(max_length=250)
    dienthoai = models.CharField(max_length=20)
    thanhpho = models.CharField(max_length=100)
    ngaytao = models.DateTimeField(auto_now_add=True)
    ngaycapnhat = models.DateTimeField(auto_now=True)    
    thanhtoan = models.BooleanField(default=False)
    hinhthucthanhtoan = models.CharField(max_length=150)

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())
    
    def get_datetime(self): 
        fix_day = datetime.strftime(self.ngaytao,"%d/%m/%y")
        return fix_day
    get_datetime.short_description = "Ngày tạo"

    def get_datetime2(self): 
        fix_day = datetime.strftime(self.ngaycapnhat,"%d/%m/%y")
        return fix_day
    get_datetime2.short_description = "Ngày cập nhật"


class OrderItem(models.Model):
    donhang = models.ForeignKey(Order, related_name='items')
    sanpham = models.ForeignKey(Blog, 
                                related_name='order_items')
    gia = models.DecimalField(max_digits=100, decimal_places=0)
    soluong = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.gia * self.soluong
