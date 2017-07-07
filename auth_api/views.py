from django.shortcuts import render
from django.contrib.auth import login,logout,authenticate
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie,get_token
from rest_framework import views, status
from rest_framework.response import Response
from .serializers import UserSerializers


class LoginView(views.APIView):

    def post(self,request):
        user = authenticate(
            username = request.data.get("username"),
            password = request.data.get("password")
        )
        if user is None or not user.is_active:
            return Response({
                "status": "Unauthorized",
                "message" : "Unauthorized Accress"
            },status=status.HTTP_403_FORBIDDEN
            )
        login(request,user)
        return Response(UserSerializers(user).data)


class LogoutView(views.APIView):

    def post(self,request):
        logout(request)
        return Response({},status=status.HTTP_204_NO_CONTENT)