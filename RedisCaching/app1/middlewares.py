from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.core.cache import cache
from django.core.exceptions import PermissionDenied
import django_redis

class RedisCache:

    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self,request):
        
        print(cache.get("3"))

        cache.set("2", "two")

        print(cache.get("2"))


        ip = request.META.get('REMOTE_ADDR')
        current_hits = cache.get(ip, 0)
        if current_hits < settings.MAX_ALLOWED_HITS_PER_IP:
            cache.set(ip, current_hits + 1)
            
        else:
            raise PermissionDenied() 
        
        req= self.get_response(request)
        return req
