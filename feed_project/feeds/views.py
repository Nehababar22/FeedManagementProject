from rest_framework import viewsets
from rest_framework.decorators import permission_classes
from feeds.filters import FeedFilter
from feeds.serializers import FeedDetailSerializer
from feeds.serializers import FeedSerializer
from feeds.models import Feed
from django.http import HttpResponse
import csv
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
import django_filters.rest_framework

# Create your views here.
class FeedViewSet(viewsets.ModelViewSet):
    """ Feed View """
    
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer 
    permission_classes=[IsAuthenticated]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_class = FeedFilter

    def perform_create(self, serializer):
        """ Set created_by user to logged-in user """
        serializer.save(created_by=self.request.user)

    def get_queryset(self):
        """ Permission for GET API """

        if self.request.user.is_superuser:
            return Feed.objects.all()               
        elif self.request.user.is_authenticated:
            return Feed.objects.filter(created_by=self.request.user)
        else:
            return Feed.objects.none()

    def get_serializer_class(self):
        """ Different serializer for same modelviewset """
        
        if self.request.method == 'GET':
            return FeedDetailSerializer
        else:
            return FeedSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated, ])
def download_report(request):
    """ Download Feeds Report API """

    if request.method == "GET":
        response = HttpResponse(content_type='text/csv')
        writer = csv.writer(response)
        writer.writerow(['title', 'content', 'publish date','Creator'])
   
        if request.user.is_superuser:
            feeds = Feed.objects.all()
        else:
            feeds = Feed.objects.filter(created_by=request.user)
           
        for feed in feeds:
            creator = feed.created_by.first_name + " " + feed.created_by.last_name
            writer.writerow([feed.title,feed.content,feed.created_at,creator])
        response['Content-Disposition'] = 'attachment; filename="adminreport.csv"'
        return response
