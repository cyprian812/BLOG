from rest_framework import serializers
from .models import Article, Category 


class articleserializers(serializers.ModelSerializer):
    
    class Meta:
        model = Article
        fields = "__all__"
        read_only_fields = ('id', "slug")
                            

class Categoryserializer(serializers.ModelSerializer):
    class Meta:
         model = Category
         fields = ("id","title", "is_published", "category")
         read_only_fields = ('id',)


class articlewithCategorySerializer(serializers.ModelSerializer):
        category = serializers.StringRelatedField()
        
        class Meta:
            model = Article
            fields = "__all__"
            read_on_fields = ('id',)


        class Meta:
            model = Article
            fields = ("id", "title", "body", "Category")
            read_only_fields = ('id',)

class articlecontentSerializer(serializers.ModelSerializer):
     
     class Meta:
          model = Article
          fields = ("id","title","body",)
          read_only_fields = ('id',)

# class CategorywitharticlesSerializer(serializers.ModelSerializer):
#      relatedarticles = serializers.SerializerMethodField()
#      myownrubbish = serializers.SerializerMethodField()

class articlecreate(serializers.ModelSerializer):
     class Meta:
        model= Article
        fields=('id','content','body',)
        read_only_fields=('id,')
     class Meta:
          model = Category
          fields = ("id","title","is_published_","relatedarticles","myownrubbish",)
          read_only_fields = ('id',)

          from rest_framework import serializers


        


def get_relatedarticles(self, obj):
    articlelist = Article.objects.filter(is_publihed=True,catogory = object.id)
    return articlecontentSerializer(articlelist,many=True).data

def get_myownrubbish (self, obj):
     return f"this is my own rubbish for id {obj.id}"

    







    

        