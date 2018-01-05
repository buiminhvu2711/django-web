from django.contrib import admin
from home.models import Home
# Register your models here.
class HomeAdmin(admin.ModelAdmin):
    list_display=('id','tenloai','get_datetime')
    # list_filter = ['ngaydang',]
fields = ( 'image_tag', 'get_datetime',)
readonly_fields = ('image_tag', 'get_datetime',)
admin.site.register(Home,HomeAdmin)
