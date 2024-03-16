from django.core.cache import cache
from configs import variable_system as vs

def get_user_info(request):
    data = request.headers.get("Authorization").replace(vs.TOKEN['type'], '')
    a = cache.get(data)
    r = cache.get(a)
    return r