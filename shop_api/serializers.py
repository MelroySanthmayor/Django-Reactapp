from rest_framework import serializers
from .models import Item
#from .models import User
from .models import Rating
from django.contrib.auth.models import User
#from rest_framework.permissions import IsAdminUser,IsAuthenticated,IsAuthenticatedOrReadOnly
from django.db.models import Avg

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id','title','description','image')








class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'],
                                        None,
                                        validated_data['password'])
        return user


class UserSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True)
    class Meta:
        model = User
        fields = ('id', 'username','items')
"""class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','password','items')
        


        '''extra_kwargs = {'password': {'write_only': True}}

        def create(self, validated_data):

            user = User(
                name = validated_data["name"],
                username = validated_data["username"]
            )
            user.set_password(validated_data["password"])
            user.save()
            return user'''


        

    #def restore_object(self, attrs, instance=None):
        # call set_password on user object. Without this
        # the password will be stored in plain text.
       # user = super(UserSerializer, self).restore_object(attrs, instance)
       # user.set_password(attrs['password'])
        # return user"""


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id','user','item','rating')