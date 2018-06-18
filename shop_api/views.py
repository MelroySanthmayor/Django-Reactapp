from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response 
from .models import Item,User,Rating
from .serializers import ItemSerializer,UserSerializer,RatingSerializer
from rest_framework.permissions import IsAdminUser,IsAuthenticated,IsAuthenticatedOrReadOnly



# Create your views here.
class ListViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = (IsAdminUser,)



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)



    


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


    def avg_rating(self):
            #rates = Rating.objects.filter(item__)
            rate = Item.objects.annotate(average_rating = Avg('Rating__rating'))
            rate.save()
            return rate
