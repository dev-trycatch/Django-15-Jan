from django.http import HttpResponse
import datetime
from django.utils.deprecation import MiddlewareMixin


# class SimpleMiddleware(MiddlewareMixin):
#     def process_request(self,request):
#         print(f"[{datetime.datetime.now()}] request url: {request.path}")
    
#     def process_response(self,request,response):
#         print(f"[{datetime.datetime.now()}] response status code : {response.status_code}")
#         return response


class BlockIPMiddleware(MiddlewareMixin):
    BLOCKED_IPS = ['127.0.0.1']

    def process_request(self,request):
        ip = request.META.get('REMOTE_ADDR')

        print(f'Your ip : {ip}')
        if ip in self.BLOCKED_IPS:
            return HttpResponse(f'Your Ip is BLocked',status = 403)


    