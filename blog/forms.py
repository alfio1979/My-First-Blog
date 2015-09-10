'''
Created on 08 set 2015

@author: alfio
'''
from .models import Post
from django import forms

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','text',)