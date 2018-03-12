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

from .models import Goods
from .serializers import GoodsSerializer
from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

class GoodsPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class GoodsListViewSet(mixins.ListModelMixin,viewsets.GenericViewSet):  #使用genercs的view快捷的传递数据
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    #pagination_class = GoodsPagination      #可以自行配置页面，但是配置文件有问题，所以放器配置，如果想要配置请参照他人代码，尤其要修改配置文件