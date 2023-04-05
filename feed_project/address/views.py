from rest_framework import viewsets
from address.serializers import AddressSerializer
from address.models import Address
from address.serializers import AddressDetailSerializer
from address.permissions import AddressPermission
from address.paginations import AddressPagination

# Create your views here.
class AddressViewSet(viewsets.ModelViewSet):
    """ Address View """
    
    queryset = Address.objects.all()
    serializer_class = AddressSerializer 
    permission_classes=[AddressPermission]
    pagination_class = AddressPagination
       
    def get_queryset(self):
        """ Permission for GET API """

        if self.request.user.is_superuser:
            return Address.objects.all()               
        elif self.request.user.is_authenticated:
            return Address.objects.filter(user= self.request.user)
        else:
            return Address.objects.none()

    def get_serializer_class(self):
        """ Different serializer for same modelviewset """

        if self.request.method == 'POST':
            return AddressDetailSerializer
        else:
            return AddressSerializer
            
