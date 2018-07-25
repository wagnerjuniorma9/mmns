# Em teoria para tirar o cash do navegador
from django.utils.cache import add_never_cache_headers

class NoCachingMiddleware(object):
    def process_response(self, request, response):
        add_never_cache_headers(response)
        return response