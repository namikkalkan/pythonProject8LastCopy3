from django.shortcuts import render
from django.http import JsonResponse
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
from django.views.generic import ListView, FormView
from django.db.models import Q
from datetime import datetime, timedelta

from .availability import check_availability
# Create your views here.

from .models import  *








def index(request):
    customer = Customer.objects.get(name='namik')
    customers = Customer.objects.all()
    products = Product.objects.all()

    d = datetime.today() - timedelta(days=3)

    p_filter = ProductFilter(request.GET,queryset=products)
    products = p_filter.qs
    has_filter = any(field in request.GET for field in set(p_filter.get_fields()))
    form = AvailabilityForm()
    books = Order_list.objects.all()
    available_products = []
    if request.method == 'POST':
        form = AvailabilityForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            if data['category'] and data['post_code'] :
                products = Product.objects.filter(Q(category=data['category']) & Q(customer__post_code=data['post_code']))
            elif data['post_code'] :
                products = Product.objects.filter(customer__post_code=data['post_code'])
            elif data['category'] :
                products = Product.objects.filter(category=data['category'])
            else:
                products =Product.objects.all()
            if data['pick_up'] and data['drop_off']:
                for product in products:
                        if check_availability(product,data['pick_up'],data['drop_off']):
                            available_products.append(product)
                products=available_products




    context = {'available_products':available_products,'form':form,'products':products,'customer':customer,'customers':customers,'p_filter':p_filter,'has_filter':has_filter,'d':d}

    return render(request,'index-updated.html', context)



def indexitem(request,pk):
    products = Product.objects.all()
    product = Product.objects.get(id=pk)
    orders = Order_list.objects.all()

    booking_list = Order_list.objects.filter(product=product)

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
            data = form.cleaned_data
            avail_list = []
            for booking in booking_list:
                if booking.rent_from >data['rent_to'] or booking.rent_to <data['rent_from']:
                     avail_list.append(True)
                else:
                    avail_list.append(False)

            if all(avail_list):

                print(data['rent_to'])
                times= data['rent_to'] - data['rent_from']
                total_cost = times * product.price
                messages.info(request, total_cost)

                '''form.save()'''

            else:
                messages.info(request, 'Sorry! it is booked, please select another date')

            '''template = render_to_string( 'confirmation.html', {'name' :request.user.customer})
            send_mail('dasd',
                         'sadsdsd',
                         settings.EMAIL_HOST_USER,
                         ['n.kalkan5506@gmail.com'],
                         )'''

        else:
            print('hataa')
            print(form.errors)

    context = {'product': product, 'products':products,'orders':orders,'form':form}
    return render(request,'product.html',context)




def sport_outdoor(request):
    products = Product.objects.filter(category='Sport-Outdoor')
    cat_name='Sport & Outdoor'

    context = {'products': products,'cat_name':cat_name}
    return render(request,'base2.html', context)

def drones_cameras(request):
    products = Product.objects.filter(category='Drones-cameras')
    cat_name = 'Drones & Cameras'

    context = {'products': products, 'cat_name': cat_name}
    return render(request, 'base2.html', context)

def electronics(request):
    products = Product.objects.filter(category='Electronics')
    cat_name = 'Electronics'

    context = {'products': products, 'cat_name': cat_name}
    return render(request, 'base2.html', context)

def home_appliances(request):
    products = Product.objects.filter(category='Home-appliances')
    cat_name = 'Home appliances'

    context = {'products': products, 'cat_name': cat_name}
    return render(request, 'base2.html', context)


def musical(request):
    products = Product.objects.filter(category='Musical-equipments')
    cat_name = 'Musical equipments'

    context = {'products': products, 'cat_name': cat_name}
    return render(request, 'base2.html', context)


def accessories(request):
    products = Product.objects.filter(category='Accessories')
    cat_name = 'Accessories'

    context = {'products': products, 'cat_name': cat_name}
    return render(request, 'base2.html', context)


def tryin(request):
    products = Product.objects.all()
    customers = Customer.objects.all()
    context = {'products': products,'customers':customers}
    return render(request,'tryin.html', context)


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
def mybookeditems(request, pk):

    customer = Customer.objects.get(id=pk)
    form = OrderForm(instance=customer)
    orders = Order_list.objects.all()

    context = {'form':form, 'customer':customer,'orders':orders}
    return render(request, 'my_booked_items.html', context)

@login_required(login_url='login')
def confirmation (request, pk):
    order = Order_list.objects.get(id=pk)


    context = { 'order': order}
    return render(request, 'confirmation.html', context)


@login_required(login_url='login')
def updateItem(request, pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES,instance=product,)
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

    context = {'form': form, "customer": customer, 'google_maps_api_key': settings.GOOGLE_API_KEY}
    return render(request, 'my_account_update.html', context)






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

