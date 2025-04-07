import django_filters
from shop.models import Product


class ProductFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    category = django_filters.CharFilter(field_name='category__name', lookup_expr='icontains')
    in_stock = django_filters.BooleanFilter(method='filter_in_stock')

    class Meta:
        model = Product
        fields = ['min_price', 'max_price', 'category', 'in_stock']

    def filter_in_stock(self, queryset, name, value):
        if value:  # اگر مقدار True باشد
            return queryset.filter(stock__gt=0)
        return queryset.filter(stock=0)
