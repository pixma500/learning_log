from django import forms
from .models import Post

class PostForm(forms.Form):
    class Meta:
        model=Post
        fields=['image','title','description']
        labels={'image':'фото','title':'название','description':'описание'}