from rest_framework import serializers
from .models import Breed, Like, Message, PetProfile, Post, Comment, Training, Transaction


class PostListSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Post
        fields = ['id','caption','image','user']

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id','caption','image','user']
        

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    class Meta:
        model = Comment
        fields = ['comment','post','user']

    def get_user(self, obj):
        return obj.user.username
        
class Likeserializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['userId','postId']
        
        
class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['text','image','senderId','receiverId']
        
class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = ['title','description','image']
        
class PetProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetProfile
        fields = ['id','name','address','breed','date_of_birth']

class TrainingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Training
        fields = ['id','title','image']
        
class TrainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Training
        fields = ['id','title','description','image','video']
        
class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['price','description','image','address','userId','phone_number']
        


