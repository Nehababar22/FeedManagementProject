from rest_framework import routers
from users.views import UserViewSet,GroupViewSet
from address.views import AddressViewSet
from feeds.views import FeedViewSet

router = routers.DefaultRouter()

router.register(r'User', UserViewSet,basename='user')
router.register(r'Groups', GroupViewSet,basename='group')
router.register(r'Address', AddressViewSet,basename='address')
router.register(r'Feed', FeedViewSet,basename='Feed')
