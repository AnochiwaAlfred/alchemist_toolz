# middleware.py
import threading

_request = threading.local()

def get_request():
    return _request.request

class RequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        _request.request = request
        response = self.get_response(request)
        return response