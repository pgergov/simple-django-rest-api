from django.shortcuts import render
from rest_framework.generics import ListAPIView

from .models import Goods
from .serializers import GoodsSerializer


class GoodsListApi(ListAPIView):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
