from django import forms
from .models import Post, Entry

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['image','title','description']
        labels={'image':'Добавить фото','title':'Название','description':'Описание'}

class EntryForm(forms.ModelForm):
    class Meta:
        model=Entry
        fields=['text',]
        labels={'text':'текст'}
        widgets = {'text': forms.Textarea(attrs={'cols': 60})}