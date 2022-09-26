from django.urls import path
from . import views

#to view static images on urls
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.index, name='index'),
    path('item/<str:pk>/', views.indexitem, name='indexitem'),
    path('camping', views.camping, name='camping'),
    path('surfing', views.surfing, name='surfing'),
    path('kayaking', views.kayaking, name='kayaking'),

    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('list-item/<str:pk>/', views.listitem, name='listitem'),
    path('my-items/<str:pk>/', views.myitem, name='myitem'),
    path('update_item/<str:pk>/', views.updateItem, name="updateitem"),
    path('my_account/<str:pk>/', views.myAccount, name="myaccount"),
    path('my_account-update/<str:pk>/', views.myAccountUpdate, name="myaccountupdate"),

    path('process_order/', views.processOrder, name="process_order"),


    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)