from typing import Tuple
from rest_framework.request import Request
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import Token 

class CookiesJWTAuthentication(JWTAuthentication):
    def authenticate(self, request) :
        access_token=request.COOKIES.get('access_token')
        
        if not access_token:
            return None
        validated_token=self.get_validated_token(access_token)
        try:
            user=self.get_user(validated_token)
        except:
            return None
        
        return (user,validated_token)