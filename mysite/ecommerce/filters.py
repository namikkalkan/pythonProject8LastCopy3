from .models import *
import django_filters
from django_filters import DateFilter,CharFilter

class ProductFilter (django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains', label='Product name')
    start_date = DateFilter(field_name='available_from' ,lookup_expr='gte', label='Pick up date')
    end_date = DateFilter(field_name='available_to', lookup_expr='lte', label= 'Drop off date')

    class Meta:
        model = Product
        fields = ['category']




