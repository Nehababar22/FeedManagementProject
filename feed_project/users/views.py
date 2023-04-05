from django.contrib.auth import  get_user_model
from users.paginations import UserPagination
from users.filters import UserFilter
from users.models import User
from rest_framework import viewsets
from users.permissions import UserPermission
from users.serializers import UserDetailSerializer
from users.serializers import GroupSerializer
from Users.serializers import UserSerializer
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Group 
from rest_framework.permissions import IsAuthenticated
import django_filters.rest_framework

# Create your views here.
User = get_user_model() 


class UserViewSet(viewsets.ModelViewSet):
    """ User View """
    
    queryset = User.objects.all()
    serializer_class = UserSerializer 
    permission_classes=[UserPermission]
    pagination_class = UserPagination
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_class = UserFilter
                  
    def perform_create(self, serializer):  
        """ Hash Password """   

        if ('password' in self.request.data):
            password = make_password(self.request.data['password'])
            serializer.save(password=password)
        else:
            serializer.save()  
      
    def get_queryset(self):
        """ Permissions for GET API """
        
        if self.request.user.is_superuser:
            return User.objects.all()               
        elif self.request.user.is_authenticated:
            if self.request.user.groups.filter(name='Admin'):
                return User.objects.filter(id = self.request.user.id)
            else:
                return User.objects.none()
        else:
            return User.objects.none()

    def get_serializer_class(self):
        """ Different serializer for same modelviewset """
        
        if self.request.method == 'GET':
            return UserDetailSerializer
        else:
            return UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """ Group View """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes=[IsAuthenticated]
       
