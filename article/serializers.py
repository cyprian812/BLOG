from rest_framework import serializers
from models import Article, Category 

class articleserializers(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ("id","title", "is_published","Catogory",)
        read_only_fields = ('id',)
                            

class Categoryserializer(serializers.Modelserializer):

    class Metal:
         model = Category
         fields = ("id","title", "is_published",)
         read_only_fields = ('id',)


class articlewithCatogorySerializer(serializers.ModelSerializer):
        Category = serializers.stringrelatedfields()

        class Meta:
            model = Article
            fields = ("id", "title", "body")
            read_only_fields = ('id',)

class articlecontentSerializer(serializers.ModelSerializer):
     
     class Meta:
          model = Article
          fields = ("id","title","body",)
          read_only_fields = ('id',)

class CategorywitharticlesSerializer(serializers.ModelSerializer):
     relatedarticles = serializers.SerializerMethodField()
     myownrubbish = serializers.SerializerMethodField()

     class Meta:
          model = Category
          fields = ("id","title","is_published_","relatedarticles","myownrubbish",)
          read_only_fields = ('id',)

def get_relatedarticles(self, obj):
    articlelist = Article.objects.filter(is_publihed=True,catogory = object.id)
    return articlecontentSerializer(articlelist,many=True).data

def get_myownrubbish (self, obj):
     return f"this is my own rubbish for id {obj.id}"

    







    

        