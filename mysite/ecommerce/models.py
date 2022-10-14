from django.db import models
from django.contrib.auth.models import User



class Customer (models.Model):
    user= models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True)
    phone=models.CharField(max_length=100, null=True)
    email=models.CharField(max_length=100, null=True)
    date_created= models.DateTimeField(auto_now_add=True)
    #driver_licence= models.ImageField( null=True, blank=True)

    address = models.CharField(verbose_name="Address", max_length=100, null=True, blank=True)
    town = models.CharField(verbose_name="Town/City", max_length=100, null=True, blank=True)
    post_code = models.CharField(verbose_name="Post Code", max_length=8, null=True, blank=True)
    country = models.CharField(verbose_name="Country", max_length=100, null=True, blank=True)
    latitude = models.CharField(verbose_name="Latitude", max_length=50, null=True, blank=True)
    longitude = models.CharField(verbose_name="Longitude", max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    CATEGORY = (
                ('Sport-Outdoor', 'Sport & Outdoor'),
                ('Drones-cameras', 'Drones & cameras'),
                ('Electronics', 'Electronics'),
                ('Home-appliances', 'Home appliances'),
                ('Musical-equipments', 'Musical equipments'),
                ('Accessories','Accessories'),
                )
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True,choices=CATEGORY)
    description = models.CharField(max_length=200, null=True, blank=True)
    date_created= models.DateTimeField(auto_now_add=True, null=True)
    available_from = models.DateTimeField(null=True)
    available_to = models.DateTimeField(null=True)
    item_pic = models.ImageField( null=True)
    item_pic_2 = models.ImageField(null=True, blank=True)
    item_pic_3 = models.ImageField(null=True, blank=True)
    item_pic_4 = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.item_pic.url
        except:
            url=''
        return url







class Order_list(models.Model):
    STATUS = (('Pending', 'Pending'),
              ('Out for delivery', 'Out_for_delivery'),
              ('Delivered', 'Delivered'))
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_ordered = models.DateTimeField(auto_now_add=True, null=True)
    complete = models.BooleanField(default=True)
    rent_from = models.DateTimeField(null=True)
    rent_to = models.DateTimeField(null=True)
    id = models.AutoField(primary_key=True)
    def __str__(self):
        return self.product.name

