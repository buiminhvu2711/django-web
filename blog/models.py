from django.db import models
from django.utils.html import format_html
from datetime import date, datetime
from django.shortcuts import render

import locale

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200)

    def __str__(self):
        return self.name

class Blog (models.Model):
    ten = models.TextField(max_length=200)
    category = models.ForeignKey(Category, related_name='blog')
    noidung = models.TextField(verbose_name='Nội dung')
    gia = models.DecimalField(decimal_places=0, max_digits=100)
    ngaydang = models.DateTimeField(auto_now_add=True)
    hinhanh= models.ImageField(null=True,blank=True)
    
    def __str__(self):
        return self.ten
    
    def image_tag(self):
        return format_html('<img src="/media/%s" width="150" height="150" />' % (self.hinhanh))
    image_tag.short_description = "Hình ảnh"
    image_tag.allow_tags = True

    def get_datetime(self): 
        fix_day = datetime.strftime(self.ngaydang,"%d/%m/%y")
        return fix_day
    get_datetime.short_description = "Ngày đăng"

    def gia_format(self):
        new = re.sub("^(-?\d+)(\d{3})", '\g<1>,\g<2>', self.gia)
        return new
    
    class Meta:
        ordering =["-id","-ngaydang"]

