from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import render, redirect

class AuthMiddleware(MiddlewareMixin):

    def process_request(self, request):
        if request.path_info in ['/login/', '/image/code/']:
            return

        info_dict = request.session.get('info')
        if info_dict:
            return

        return redirect('/login/')