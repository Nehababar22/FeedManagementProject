from users.models import User
from rest_framework import  serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from address.models import Address

User = get_user_model()  


class UserSerializer(serializers.ModelSerializer):
    """  serializer for User model """

    class Meta:
        model = User
        exclude = ('groups', )


class GroupSerializer(serializers.ModelSerializer):
    """  Serializer for Group model """
    
    class Meta:
        model = Group
        fields = ['name']

     
class UserDetailSerializer(serializers.ModelSerializer):
    address = serializers.SerializerMethodField('get_address')
    groups = GroupSerializer(many=True)

    def get_address(self,obj):
        """ customize fields for User API """    

        results = Address.objects.filter(user=obj
        ).values('street','city','state','country','user').first()
        return results

    class Meta:
        model = User
        exclude = ('password', )
                        
