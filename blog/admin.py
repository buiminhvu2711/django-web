from django.contrib import admin
from blog.models import Blog,Category
# Register your models here.
class Sanpham(admin.ModelAdmin):
    list_display = ["id","ten","image_tag","get_datetime"]

fields = ( 'image_tag', 'get_datetime',)
readonly_fields = ('image_tag', 'get_datetime',)

admin.site.register(Blog,Sanpham)
admin.site.site_header = 'Trang Quản Lý - Django '
admin.site.site_title = 'Quản lý sản phẩm'

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category, CategoryAdmin)