from rest_framework.pagination import PageNumberPagination

class UserPagination(PageNumberPagination):
    """ pagination for user api """
    page_size = 10  