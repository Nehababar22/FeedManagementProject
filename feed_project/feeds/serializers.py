from users.models import User
from feeds.models import Feed
from rest_framework import  serializers

class FeedSerializer(serializers.ModelSerializer):
    """  serializer for Feed model """
                           
    class Meta:
        model = Feed
        fields = "__all__"


class FeedDetailSerializer(serializers.ModelSerializer):
    created_by = serializers.SerializerMethodField('get_created_by')

    def get_created_by(self,obj):
        """ customize fields for Feed API """
        
        results = User.objects.filter(feed=obj
        ).values('id','first_name','last_name','username','email','groups').first() 
        return results  

    class Meta:
        model = Feed
        fields = "__all__"
