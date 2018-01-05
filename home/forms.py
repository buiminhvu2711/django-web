from django import forms
import re
from django.contrib.auth.models import User #kiểm tra tồn tại trong database chưa
from django.core.exceptions import ObjectDoesNotExist #lỗi không tồn tại
class RegistationForm(forms.Form):
    username = forms.CharField(label="Tài khoản", max_length=30)
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Mật khẩu", widget=forms.PasswordInput())
    password2 = forms.CharField(label="Nhập lại mật khẩu", widget=forms.PasswordInput())
    keep_logged = forms.BooleanField(required=False, label="Lưu đăng nhập")
    

    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2:  
                return password2
        raise forms.ValidationError("Mật khẩu không phù hợp")

    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$',username): # \w toàn ký tự thường.
            raise forms.ValidationError("Tài khoản có ký tự đặc biệt")
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError("Tài khoản đã tồn tại")

