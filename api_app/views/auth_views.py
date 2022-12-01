from rest_framework.viewsets import ViewSet
from helpers.response import *
from ..validations.auth_validate import *
import jwt
from configs.variable_response import *
from django.db.models import Q
from configs.variable_system import *
import bcrypt
from django.core.cache import cache
from datetime import datetime
import uuid
from ..serializers.user_serializer import *

class AuthView(ViewSet):
    # ham dang nhap
    def login(self, request):
        data = request.data.copy()
        
        # check input request
        validate = LoginValidate(data=data)
        if not validate.is_valid():
            return validate_error(validate.errors)
        
        username = data[U]
        password = data[P]
        
        # kiem tra ton tai user
        user = self.query_user_exists(username)
        if not user.exists():
            return response_data(status=STATUS['NO_DATA'], message=str(username) + ERROR['not_exists'])
        
        # kiem tra password
        b_password = user.values(P)[0][P]
        if not self.check_passwork(password, b_password):
            return response_data(status=STATUS['FAIL_REQUEST'],message=ERROR['wrong_password'])
        
        # tao token
        a_token, r_token = self.create_token()
        serializer = UserSerializer(user, many=True)
        redis_data = serializer.data[0]
        
        # set data redis
        self.set_token_redis(a_token=a_token, r_token=r_token, data=redis_data)
        return response_data({
            'access_token': a_token,
            'refresh_token':r_token  
        }, message=SUCCESS['login'])
        
    # ham lam moi session
    def refresh_token(self, request):
        data = request.data.copy()
        
        validate = RefreshTokenValidate(data=data)
        if not validate.is_valid():
            return validate_error(validate.errors)
        
        # kiem tra refresh token cu
        redis_data = cache.get(data['refresh_token'])
        if redis_data is None:
            return response_data(status=STATUS['INPUT_INVALID'],message=ERROR['refresh_token'])
        
        # xoa phien dang nhap cu
        self.delete_token(redis_data['token'], data['refresh_token'])
        
        # tao token
        a_token, r_token = self.create_token()
        
        # set data redis
        self.set_token_redis(a_token=a_token, r_token=r_token, data=redis_data)
        return response_data({
            'access_token': a_token,
            'refresh_token':r_token  
        }, message=SUCCESS['refresh_token'])
        
    
    # duoi day la ham not request
    def hash_password(self, s):
        byte_pwd = s.encode('utf-8')
        my_salt = bcrypt.gensalt()
        pwd_hash = bcrypt.hashpw(byte_pwd, my_salt)
        return str(pwd_hash)
    
    def check_passwork(self, password, b_password):
        return bcrypt.checkpw(password.encode('utf-8'), b_password.encode('utf-8'))
    
    def create_token(self):
        token = {
            'datetime': str(datetime.now()),
            'session': str(uuid.uuid1())
        }
        access_token = self.jwt_encode(data=token, key=TOKEN['public_key'])
        refresh_token = self.jwt_encode(data=token, key=TOKEN['private_key'])
        return access_token.decode('utf-8'), refresh_token.decode('utf-8')
        # return str(access_token).replace("'","").lstrip('b'), str(refresh_token).replace("'","").lstrip('b')
    
    def jwt_encode(self, data, key):
        return jwt.encode(data, key, algorithm=TOKEN['hash'])
    
    def query_user_exists(self, username):
        return User.objects.filter(Q(username=username) | Q(email=username)).filter(deleted_at__isnull=True)
    
    def set_token_redis(self, a_token, r_token, data):
        data['token'] = a_token
        cache.set(a_token, r_token, timeout=TOKEN['tls_access_token'])
        cache.set(r_token, data, timeout=TOKEN['tls_refresh_token'])
        
    def delete_token(self, a_token, r_token):
        cache.delete(a_token)
        cache.delete(r_token)
    
    def get_data_token(self, request):
        data = request.data.copy()
        a = cache.get(data['access_token'])
        b = cache.get(a)
        return response_data({
            'a':a,
            'b':b
        })
