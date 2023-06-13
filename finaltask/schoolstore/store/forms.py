from django import forms
from .models import Order, Department, Course,Materials

class UserProfileForm(forms.ModelForm):
    # Define your form fields and widgets

    class Meta:
        model = Order
        fields = ['name', 'dob', 'age', 'gender', 'phnumber', 'email', 'address', 'department', 'course', 'purpose', 'materials_provide']
        widgets = {
            'materials_provide': forms.CheckboxSelectMultiple,
        }
