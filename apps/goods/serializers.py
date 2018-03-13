

#写序列化，为了view使用序列化函数
from rest_framework import serializers
from .models import Goods,GoodsCategory

class CategorySerializer3(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = "__all__"
class CategorySerializer2(serializers.ModelSerializer):
    sub_cat = CategorySerializer3(many=True) #读取多组数据，所以要写many = true
    class Meta:
        model = GoodsCategory
        fields = "__all__"
class CategorySerializer(serializers.ModelSerializer): #依靠parent_category中的related_name来反向序列化数据库
    sub_cat = CategorySerializer2(many=True)
    class Meta:
        model = GoodsCategory
        fields = "__all__"


class GoodsSerializer(serializers.ModelSerializer):
    '''name = serializers.CharField(required=True,max_length=100)
    goods_front_image = serializers.ImageField(default=True)
    click_num = serializers.CharField(required=True)

    def create(self, validated_data):  #验证前端传递过来的数据
        """
        create and return a new snippet instance,given the validated data.
        :param validated_data:
        :return:
        """
        return Goods.objects.create(**validated_data)'''
    category = CategorySerializer() #外键实例化
    class Meta:
        model = Goods
        #fields = ('name', 'click_num', 'goods_desc','add_time')
        fields = "__all__" #取出所有的字段


