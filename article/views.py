from django.shortcuts import render
from rest_framework import generics
from article import serializers

# Create your views here.
from .models import Category, Article
# from article import serializers


class categorylistview(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.Categoryserializer


class categoryeditedview(generics.RetrieveDestroyAPIView):
            queryset= Article.objects.all()
            serializer_class= serializers.Categoryserializer


class articlelistview(generics.ListAPIView):
       queryset = Article.objects.all()
       serializer_class= serializers.articlewithCategorySerializer
       

class ArticleCreateView(generics.CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = serializers.articleserializers


class categoryeditedviewwithSlug(generics.RetrieveUpdateDestroyAPIView):
       queryset = Article.objects.all()
       serializer_class= serializers.articleserializers
       lookup_field= 'slug'


class categorywitharticleslistview(generics.ListAPIView):
       queryset= Article.objects.all()
       serializer_class= serializers.articleserializers

# class UserDetailView(generics.RetrieveAPIView):
#     queryset = Article.objects.all()
#     serializer_class = serializers.UserSerializer
  
# class UserCreateserializer(generics.CreateAPIView):
#     queryset =Article.objects.all()
#     serializer_class =serializers.Article


