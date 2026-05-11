from django import forms
from .models import Post

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'categories', 'published_at']
        widgets = {
            'title' : forms.TextInput(attrs = { 'class' : 'form-control'}),
            'body' : forms.Textarea(attrs={'class': 'form-control'}),
            'categories' : forms.SelectMultiple(attrs = { 'class' : 'form-control'}),
            'published_at': forms.DateTimeInput(attrs={'class': 'form-control'}),
        }