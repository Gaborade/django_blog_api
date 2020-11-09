from rest_framework import generics 
from .models import Post
from .serializers import PostSerializer
from .permissions import IsAuthorOrReadOnly
# Create your views here.
class PostList(generics.ListCreateAPIView):
    # generics.ListCreateAPIView for post requests for a single model instance
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    # Used for read-write-delete endpoints to represent a single model instance
    permission_classes = (IsAuthorOrReadOnly,)  # view level permission that only allows
    # users of posts to have write-update-delete operations
    queryset = Post.objects.all()
    serializer_class = PostSerializer
