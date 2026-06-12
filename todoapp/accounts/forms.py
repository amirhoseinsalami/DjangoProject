from django import forms
from .models import Profile

class UpdateProfilePhotoForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['photo']
        widgets = {
            'photo': forms.ClearableFileInput(attrs={
                'class': 'form-control',
            })
        }
