from address.models import Address
from rest_framework import  serializers
   
class AddressSerializer(serializers.ModelSerializer):
    """  Serializer for Address model """
  
    class Meta:
        model = Address
        fields = "__all__"


class AddressDetailSerializer(serializers.ModelSerializer):

    def validate_user(self, user):
        """ Check user Address has already exists """

        is_already_exists = Address.objects.filter(user=user).exists()
        if is_already_exists:
            raise serializers.ValidationError('already exists')
        return user

    class Meta:
        model = Address
        fields = "__all__"    
   
