from django.shortcuts import render

from rest_framework.generics import CreateAPIView, ListCreateAPIView
from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from .permissions import IsPostOrIsAuthenticated

class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [IsPostOrIsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
 
        serializer.validated_data['is_superuser']=False
        serializer.validated_data['is_staff']=False
        serializer.validated_data['is_active']=True
 
        user = serializer.save()
 
        data = serializer.data
        if Token.objects.filter(user=user).exists():
            token = Token.objects.get(user=user)
            data['token'] = token.key
        else:
            data['token'] = 'No token created for this user!!!'
 
        headers = self.get_success_headers(serializer.data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)

@api_view(['POST'])
@permission_classes([IsPostOrIsAuthenticated])
def logout(request):
 
    request.user.auth_token.delete()
    data = {
        'message' : 'Başarıyla çıkış yapıldı!',
    }
    return Response(data,status=status.HTTP_200_OK)

from django.contrib.auth.views import PasswordResetConfirmView as AuthPasswordResetConfirmView
from django.urls import reverse_lazy
from django.contrib import messages

class MyPasswordResetConfirmView(AuthPasswordResetConfirmView):
    success_url = reverse_lazy('password_reset_complete')   

    def dispatch(self, *args, **kwargs):
        self.uid = kwargs['uidb64']
        self.token = kwargs['token']
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):

        response = super().form_valid(form)
        # messages.warning(self.request, 'Below input the new password and then input it again.')
        return response

    def get(self, request, *args, **kwargs):

        return super().get(request, *args, **kwargs)

 