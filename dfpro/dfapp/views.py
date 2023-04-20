from django.http import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import serializers
from .models import API

class APISerializer(serializers.ModelSerializer):
    class Meta:
        model = API
        fields = '__all__'

def home(request):
    return HttpResponse(f'<body style="background-color:blue"><div style="text-align:center; color:red; padding-top: 40vh;  margin: 0; "><h1>Ecommerce API</h1></div></body>')

class MPN(LimitOffsetPagination):
    default_limit = 10
    limit_query_param = 20
    max_limit = 50
    offset_query_param = 'p'


class List_and_Create_Data(ListCreateAPIView):
    queryset = API.objects.all()
    serializer_class = APISerializer
    pagination_class = MPN
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'discounted_price', 'Product_image',
                        'Description', 'Original_price',
                        'item_number', 'attribute_dic']


class Retrieve_Update_Delete_Data(RetrieveUpdateDestroyAPIView):
    queryset = API.objects.all()
    serializer_class = APISerializer
    pagination_class = MPN
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'discounted_price', 'Product_image',
                        'Description', 'Original_price',
                        'item_number', 'attribute_dic']
