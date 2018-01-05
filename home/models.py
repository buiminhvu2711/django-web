from django.db import models
from django.shortcuts import render
from django.utils.html import format_html
from datetime import date, datetime
import locale
import datetime

# Create your models here.
class Home (models.Model):
    tenloai = models.TextField(max_length=200)
    nguongoc = models.TextField()
    ngaydang= models.DateTimeField(auto_now_add=True)
    img_nguongoc= models.ImageField(null=True,blank=True)
    tinhcam = models.TextField()
    img_tinhcam = models.ImageField(null=True,blank=True)
    tinhcach = models.TextField()
    img_tinhcach = models.ImageField(null=True,blank=True)
    
    def __str__(self):
        return self.tenloai

    def get_datetime(self): 
        fix_day = datetime.datetime.strftime(self.ngaydang,"%d/%m/%y")
        return fix_day
    get_datetime.short_description = "Ngày đăng"

    def image_tag(self):
        return format_html('<img src="/media/%s" width="150" height="150" />' % (self.img_nguongoc))
    image_tag.short_description = "Hình ảnh"
    image_tag.allow_tags = True

    class Meta:
        ordering = ["-id",]
    

   
