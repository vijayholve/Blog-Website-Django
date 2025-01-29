from django import forms
from blogs.models import Category,Blogs,CKBlog
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django_ckeditor_5.fields import CKEditor5Field


class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields = '__all__'

class CKBlogPostForm(forms.ModelForm):
    class Meta:
        model=CKBlog
        fields = ['title', 'content']
        widgets = {
            'content': CKEditor5Field(),
        }
class BlogPostForm(forms.ModelForm):
    class Meta:
        model=Blogs
        fields = ('title','category','blog_image','short_description','blog_body','status','is_feacherd')



class AddUserForm(UserCreationForm):
    class Meta:
        model=User
        fields = ('username','email','first_name','last_name','is_active','is_staff','is_superuser','groups','user_permissions')
        

class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','email','first_name','last_name','is_active','is_staff','is_superuser','groups','user_permissions')
