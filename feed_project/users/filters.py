from users.models import User
import django_filters

class UserFilter(django_filters.FilterSet):
    """" filtering for user api """

    username = django_filters.CharFilter(lookup_expr='iexact',field_name="username")
    first_name = django_filters.CharFilter(lookup_expr='iexact',field_name="first_name")
    last_name = django_filters.CharFilter(lookup_expr='iexact',field_name="last_name")
    email = django_filters.CharFilter(lookup_expr='iexact',field_name="email")

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name','email']
        
