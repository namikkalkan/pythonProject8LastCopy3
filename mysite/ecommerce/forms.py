from django.forms import ModelForm
from .models import  *
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class DateForm(forms.Form):
    date = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])

class OrderForm(ModelForm):

    rent_from = forms.DateTimeField(widget=forms.DateInput(attrs={'placeholder':'Pick up from'}))
    class Meta:
        model = Order
        fields = '__all__'

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

