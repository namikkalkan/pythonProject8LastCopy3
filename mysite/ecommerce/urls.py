from django.urls import path
from . import views

#to view static images on urls
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.index, name='index'),
    path('item/<str:pk>/', views.indexitem, name='indexitem'),

    path('sport-outdoor/', views.sport_outdoor, name='sport_outdoor'),
    path('drone-cameras/', views.drones_cameras, name='drone_cameras'),
    path('electronics/', views.electronics, name='electronics'),
    path('home-appliances/', views.home_appliances, name='home_appliances'),
    path('musical/', views.musical, name='musical'),
    path('accessories/', views.accessories, name='accessories'),

    path('faq/', views.tryin, name='tryin'),


    path('list-item/<str:pk>/', views.listitem, name='listitem'),
    path('my-items/<str:pk>/', views.myitem, name='myitem'),
    path('my-booked-items/<str:pk>/', views.mybookeditems, name='mybookeditems'),
    path('update_item/<str:pk>/', views.updateItem, name="updateitem"),
    path('my_account/<str:pk>/', views.myAccount, name="myaccount"),
    path('my_account-update/<str:pk>/', views.myAccountUpdate, name="myaccountupdate"),
    path('process_order/', views.processOrder, name="process_order"),
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),


    path('confirmation/<str:pk>/', views.confirmation, name='confirmation'),



]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)