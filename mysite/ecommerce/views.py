from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from PIL import Image
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decoraters import *
from django.contrib.auth.models import Group
from .forms import *
from  .filters import *

from django.core.mail import send_mail
from  django.conf import settings
from  django.template.loader import render_to_string

from django.forms.models import model_to_dict
import json

from datetime import datetime, timedelta


from django.forms import inlineformset_factory
# Create your views here.

def index(request):
    customer = Customer.objects.get(name='namik')
    customers = Customer.objects.all()
    products = Product.objects.all()

    d = datetime.today() - timedelta(days=3)

    p_filter = ProductFilter(request.GET,queryset=products)
    products = p_filter.qs
    has_filter = any(field in request.GET for field in set(p_filter.get_fields()))

    context = {'products':products,'customer':customer,'customers':customers,'p_filter':p_filter,'has_filter':has_filter,'d':d}

    return render(request,'index.html', context)

def indexitem(request,pk):
    products = Product.objects.all()
    product = Product.objects.get(id=pk)
    orders = Order_list.objects.all()
    if request.user.is_authenticated:
        customer = request.user.customer
        form = OrderForm(initial={'product': product,'customer':customer})
    else:
        form = OrderForm(initial={'product': product})
    if request.method == 'POST':
        form = OrderForm(request.POST)
        datepicker = request.POST.get('rent_from')
        datepicker2 = request.POST.get('rent_to')


        #Order.objects.create(customer=customer, product=product, rent_to=datepicker,rent_from=datepicker2 )

        if form.is_valid():

            form.save()
            '''template = render_to_string( 'confirmation.html', {'name' :request.user.customer})
            send_mail('dasd',
                         'sadsdsd',
                         settings.EMAIL_HOST_USER,
                         ['n.kalkan5506@gmail.com'],
                         )'''
            return redirect('/')
        else:
            print('hataa')
            print(form.errors)

    context = {'product': product, 'products':products,'orders':orders,'form':form}
    return render(request,'index-item.html',context)

def surfing(request):
    products = Product.objects.all()
    context = {'products': products}

    return render(request,'surfing.html', context)

def camping(request):
    products = Product.objects.all()
    context = {'products':products}

    return render(request,'camping.html', context)

def kayaking(request):
    products = Product.objects.all()
    context = {'products':products}

    return render(request,'kayaking.html', context)


@login_required(login_url='login')
def listitem(request, pk):
    customer = Customer.objects.get(id=pk)
    form = ProductForm(initial ={'customer':customer})

    if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            print('hataa')
            print(form.errors)

    context = {'form': form,'customer':customer}
    return render(request, 'list_item.html', context)



@login_required(login_url='login')
def myitem(request, pk):

    customer = Customer.objects.get(id=pk)
    form = ProductForm(instance=customer)
    products = Product.objects.all()

    context = {'form':form, 'customer':customer,'products':products}
    return render(request, 'my_item.html', context)



@login_required(login_url='login')
def updateItem(request, pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form, "item": product, "order_c": product.customer}
    return render(request, 'update-item.html', context)



def processOrder (request):

    print('data', request.body)
    return JsonResponse('Confirmed', safe=False)


@login_required(login_url='login')
def myAccount(request, pk):
    customer = Customer.objects.get(id=pk)
    form = CustomerForm(instance=customer)

    context = {'form': form, "customer": customer}
    return render(request, 'my_account.html', context)



@login_required(login_url='login')
def myAccountUpdate(request, pk):
    customer = Customer.objects.get(id=pk)
    form = CustomerForm(instance=customer)

    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form, "customer": customer}
    return render(request, 'my_account_update.html', context)








def store(request):
    context = {}
    return render(request, 'store.html')

def cart(request):
    context = {}
    return render(request, 'cart.html')

def checkout(request):
    context = {}
    return render(request, 'checkout.html')






@unauthenticated_user
def registerPage(request):

    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            username = form.cleaned_data.get('username')
            email= form.cleaned_data.get('email')

            group = Group.objects.get(name='customer')
            user.groups.add(group)
            Customer.objects.create(user=user, name=username,email=email)

            messages.success(request, 'Succesfully created ' + username)
            return redirect('login')

    context = {'form': form}
    return render(request, 'register.html', context)

@unauthenticated_user
def loginPage(request):


    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'login.html', context)

@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('index')

