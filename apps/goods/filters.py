import django_filters
from .models import Goods
from django.db.models import Q


class GoodsFilter(django_filters.rest_framework.FilterSet):
    """
    商品过滤类,自定义过滤器
    """
    pricemin = django_filters.NumberFilter(name="shop_price",lookup_expr='gt')#大于等于
    pricemax = django_filters.NumberFilter(name="shop_price",lookup_expr='lt')#小于等于
    #name = django_filters.CharFilter(name="name",lookup_expr='icontains')#模糊查询，不写icontains会进行准确匹配
    top_category = django_filters.NumberFilter(method='top_category_filter')

    def top_category_filter(self, queryset, name, value):#自定义过滤，根据类别进行过滤
        return queryset.filter(Q(category_id=value) | Q(category__parent_category_id=value) | Q(
            category__parent_category__parent_category_id=value))


    class Meta:
        model = Goods
        fields = ['pricemin', 'pricemax','is_hot', 'is_new']


