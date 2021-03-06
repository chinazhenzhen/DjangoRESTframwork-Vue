"""Mxshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
#from django.contrib import admin
import xadmin

from Mxshop.settings import MEDIA_ROOT
from django.views.static import serve
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter  #利用defaultroute配置url
from rest_framework.authtoken import views   #token
from rest_framework_jwt.views import obtain_jwt_token   #jwt token认证模式

from goods.views import GoodsListViewSet,CategoryViewSet

router = DefaultRouter()

#配置goods的url
router.register(r'goods',GoodsListViewSet,base_name="goods")

#配置category的url
router.register(r'categorys',CategoryViewSet,base_name="categorys")

#from goods.views_base import GoodsListView



urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^media/(?P<path>.*)$',serve,{"document_root": MEDIA_ROOT}),

    url(r'^',include(router.urls)),

    url(r'docs/',include_docs_urls(title="购物平台")),

    url(r'^api-auth/', include('rest_framework.urls')), #include 存在于django.conf.urls 中

    #url(r'^api-token-auth/', views.obtain_auth_token),  #drf自带token认证

    #jwt的认证接口
    url(r'^login/', obtain_jwt_token),
]
