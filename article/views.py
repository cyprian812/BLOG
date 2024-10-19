from django.shortcuts import render
from rest_framework import generics
# Create your views here.
from .models import Category, Article
from article import serializers

class categorylistview(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.Categoryserializer

class categorycreateview(generics.CreateAPIView):
        queryset= Category.objects.all
        serializer_class= serializers.Categoryserializer

class categoryeditedview(generics.RetrieveDestroyAPIView):
            queryset= Article.objects.all()
            serializer_class= serializers.articlewithCatogorySerializer

class articlecreateview(generics.CreateAPIView):
    queryset= Article.objects.all()
    serializer_class= serializers.articlewithcategoryserializer

class categoryeditedviewwithSlug(generics.RetrieveUpdateDestroyAPIView):
       queryset = Article.objects.all()
       serializer_class= serializers.articleserializers
       lookup_field= 'slug'

class categorywitharticleslistview(generics.ListAPIView):
       queryset= Article.objects.all()
       serializer_class= serializers.CategorywitharticlesSerializer





