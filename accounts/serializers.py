
from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.tokens import RefreshToken, TokenError


class customuser_serializer(serializers.ModelSerializer):
    class Meta:
        model= CustomUser
        fields = '__all__' 

class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        max_length=128, min_length=6, write_only=True)

    class Meta:
        model = CustomUser
        fields = ('email','username','password','first_name','last_name','number')

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        max_length=128, min_length=6, write_only=True)

    class Meta:
        model = CustomUser
        fields = ('email', 'password')

class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    default_error_message = {
        'bad_token': ('Token is expired or invalid')
    }

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):

        try:
            RefreshToken(self.token).blacklist()

        except TokenError:
            self.fail('bad_token')        

class forget_password_serializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email',) 

class Reset_password_serializer(serializers.ModelSerializer):
    class Meta:
        model = change_password
        fields =('new_password','confirm_password')

class Social_serializer(serializers.ModelSerializer):
    class Meta:
        model = Social
        fields ='__all__'


class About_serializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields ='__all__'


class Profile_Pic_serializer(serializers.ModelSerializer):
    class Meta:
        model = Profile_Pic
        fields ='__all__'


class Comment_serializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class User_Post_serializer(serializers.ModelSerializer):
    comment_set = Comment_serializer(many=True, read_only=True)
    class Meta:
        model = Post
        fields = ['post_name','tag_name','blog','post_header','post_content','images','document','likes','created_date','update_date','is_active','user','comment_set']
        

class BlogSerializer(serializers.ModelSerializer):
    group_set = Profile_Pic_serializer(many=True, read_only =True)
    class Meta:
        model = Blog
        fields = ['tag_name','blog_name','created_date','update_date','user','images','group_set']
        
    def create(self, validated_data):
        return Blog.objects.create(**validated_data)

