from .serializers import BookSerializer, BookMiniSerializer, CharacterListSerializer
from .models import Book, Character
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class BookViewSet(viewsets.ModelViewSet): 
    serializer_class = BookMiniSerializer
    queryset = Book.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = BookSerializer(instance)
        return Response(serializer.data)
    
class CharacterViewSet(viewsets.ModelViewSet): 
    serializer_class = CharacterListSerializer
    queryset = Character.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = CharacterListSerializer(instance)
        return Response(serializer.data)