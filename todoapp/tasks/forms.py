from django import forms
from .models import Task

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'categories', 'priority', 'status', 'due_date']
        widgets = {
            'title' : forms.TextInput(attrs={ 'class' : 'form-control'}),
            'description' : forms.Textarea(attrs={'class': 'form-control'}),
            'categories' : forms.SelectMultiple(attrs={ 'class' : 'form-control'}),
            'priority': forms.RadioSelect(attrs={'class': 'form-control'}),
            'status': forms.RadioSelect(attrs={'class': 'form-control'}),
            'due_date': forms.DateTimeInput(attrs={'class': 'form-control'}),
        }

