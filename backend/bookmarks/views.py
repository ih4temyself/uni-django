from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from .models import Bookmark, Category
from .serializers import BookmarkSerializer, CategorySerializer


class BookmarkViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]  
    queryset = Bookmark.objects.all() 
    serializer_class = BookmarkSerializer

    def get_queryset(self):
        return Bookmark.objects.filter(user=self.request.user)
    
    def retrieve(self, request, pk=None):
        bookmark = get_object_or_404(self.queryset, pk=pk)
        serializer = self.get_serializer(bookmark)
        return Response(serializer.data)


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
