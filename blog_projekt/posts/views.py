from rest_framework import generics
from .models import Post
from .serializers import PostSerializer

# Create your views here.
class PostList(generics.ListCreateAPIView):
    # generics.ListCreateAPIView for post requests for a single model instance
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    # Used for read-write-delete endpoints to represent a single model instance
    queryset = Post.objects.all()
    serializer_class = PostSerializer
