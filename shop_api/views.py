from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response 
# Create your views here.
 class ListViewSet(viewsets.ViewSet):
     def list(self,request):
         return Response("Success!")