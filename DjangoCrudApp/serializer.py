from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework import serializers,validators
from .models import Posts
from django.contrib.auth.hashers import make_password,check_password
"""
class NPKSerializer(serializers.ModelSerializer):
    GPS=GPS
class Meta: 
        model=NPK
        fields='__all__'
class NDvi(serializers.ModelSerializer):
    GPS=GPS
    class Meta:
        model=NDvi
        fields='__all__' 
class NPKard(serializers.ModelSerializer):
    GPS=GPS
    class Meta:
        model=NPKard
        fields='__all__' 
class Camera(serializers.ModelSerializer):
    GPS=GPS
    class Meta:
        
        model=Camera
        fields='__all__'                    
"""
class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model=Posts
        #fields=('ticker','volume')
        fields='__all__'
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('username','password','email','first_name','last_name')
    extra_kwargs={
        "password":{"write_only":True},
        "email":{
        "required":True,
        "validators":[
        validators.UniqueValidator(
        User.objects.all(),"A user with that Email already exist"
        )
        ]
        }
    }
    def create(self, validated_data):
        username=validated_data.get('username')
        password=make_password(validated_data.get('password'))
        email=validated_data.get('email')
        first_name=validated_data.get('first_name')
        last_name=validated_data.get('last_name')
        user=User.objects.create(
            username=username,
            password=password,
            email=email,
            first_name=first_name,
            last_name=last_name
        )
        return user
