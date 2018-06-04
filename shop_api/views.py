from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response 
from .models import Item
from .serializers import ItemSerializer
# Create your views here.
class ListViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer