from feeds.models import Feed
import django_filters

class FeedFilter(django_filters.FilterSet):
    """" filtering for feed api """

    class Meta:
        model = Feed
        fields = ['created_by']
