import django_filters
from .models import Goods


class GoodsFilter(django_filters.rest_framework.FilterSet):
    """
    商品过滤类,自定义过滤器
    """
    price_min = django_filters.NumberFilter(name="shop_price",lookup_expr='gt')#大于等于
    price_max = django_filters.NumberFilter(name="shop_price",lookup_expr='lt')#小于等于
    #name = django_filters.CharFilter(name="name",lookup_expr='icontains')#模糊查询，不写icontains会进行准确匹配


    class Meta:
        model = Goods
        fields = ['price_min', 'price_max']


