"""Post views."""

# Django Rest Framework
from rest_framework import viewsets

# Own
from lessons.api.serializers import PostModelSerializer
from lessons.api.models import Post

class PostViewSet(viewsets.ModelViewSet):
    """ Post view set
        Handle all CRUD requests
    """

    queryset = Post.objects.all()
    serializer_class = PostModelSerializer
    
       