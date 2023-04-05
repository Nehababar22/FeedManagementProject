from rest_framework.pagination import PageNumberPagination

class AddressPagination(PageNumberPagination):
    """ pagination for address api """
    page_size = 10  