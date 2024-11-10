from rest_framework import serializers
from .models import Note
from django.contrib.auth.models import User


class RegistrationSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=['username','email','password']
        
    def create(self,validated_data):
        user=User(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username']

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Note
        fields=['id','description']