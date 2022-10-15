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
        'description': forms.Textarea(attrs={'rows': 4}),

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



class AvailabilityForm(forms.Form):
    CATEGORY = (
        ('','All Products'),
        ('Sport-Outdoor', 'Sport & Outdoor'),
        ('Drones-cameras', 'Drones & cameras'),
        ('Electronics', 'Electronics'),
        ('Home-appliances', 'Home appliances'),
        ('Musical-equipments', 'Musical equipments'),
        ('Accessories', 'Accessories'),
    )

    pick_up= forms.DateTimeField(required=False, input_formats=["%Y-%m-%dT%H:%M"])
    drop_off = forms.DateTimeField(required=False, input_formats=["%Y-%m-%dT%H:%M"])
    category = forms.ChoiceField(required=False,choices=CATEGORY)
    post_code = forms.CharField(required=False)