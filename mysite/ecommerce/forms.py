from django.forms import ModelForm
from .models import  *
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class DateForm(forms.Form):
    date = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])

class OrderForm(ModelForm):

    #rent_from = forms.DateTimeField()
    #rent_to = forms.DateTimeField()
    class Meta:
        model = Order_list
        fields = '__all__'

        widgets = {
            'rent_from': forms.TextInput(attrs={'placeholder': 'month/day/year'}),
            'rent_to': forms.TextInput(attrs={'placeholder': 'month/day/year'}),
            'customer': forms.TextInput(attrs={'type': 'hidden'}),
            'product': forms.TextInput(attrs={'type': 'hidden'}),
            'id': forms.TextInput(attrs={'type': 'hidden'}),
            'complete': forms.TextInput(attrs={'type': 'hidden'}),
        }
class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

        widgets = {
        'customer': forms.TextInput(attrs={'type': 'hidden'}),
    }

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user']

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

