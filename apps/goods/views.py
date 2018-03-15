'''from .serializers import GoodsSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics


from .models import Goods

class GoodsListView(APIView):
       def get(self,request,format=None):
        goods = Goods.objects.all()[:10]
        goods_serializer = GoodsSerializer(goods,many=True)
        return Response(goods_serializer.data)

    def post(self, request, format=None):  #从前端接收json数据，drf不用判断post还是get数据，直接处理
        serializer = GoodsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()    #调用save函数调用的是序列中的create方法
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    '''

from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import filters #去drf的filters中的searchfilrter官方文档实现更多搜索功能
from rest_framework.pagination import PageNumberPagination
from rest_framework.authentication import TokenAuthentication   #token认证
from django_filters.rest_framework import DjangoFilterBackend    #django-filters的用法，详见官方文档,可以实现各种模糊搜索

from .serializers import GoodsSerializer,CategorySerializer
from .models import Goods,GoodsCategory
from .filters import GoodsFilter

class GoodsPagination(PageNumberPagination):#用来配置view页面
    page_size = 12
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100

class GoodsListViewSet(mixins.ListModelMixin,viewsets.GenericViewSet):  #使用genercs的view快捷的传递数据
    """
    分页 搜索 过滤 排序
    """
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination      #可以自行配置页面，但是配置文件有问题，所以放器配置，如果想要配置请参照他人代码，尤其要修改配置文件
    #authentication_classes = (TokenAuthentication,) #配置token

    filter_backends = (DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter) #利用drf中的SearchFilter实现模糊搜索
    filter_class = GoodsFilter
    search_fields = ('name', 'goods_brief')#从两个属性中模糊搜索
    ordering_fields = ('shop_price','sold_num') #排序

class CategoryViewSet(mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):#加入mixins.RetrieveModelMixin就可以获取莫一个商品的详情
    """
        list:
            商品分类列表数据
        retrieve:
            获取商品分类详情
    """
    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = CategorySerializer  #对于这种View必须传入相应的serializer序列化

