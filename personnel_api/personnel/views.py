from django.shortcuts import render
from .serializers import Department, DepartmentSerializer, Personnel, PersonnelSerializer, DepartmentPersonnelSerializer
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .permissions import IsAdminOrReadOnly
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class DepartmentListCreateView(ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = (
        IsAuthenticated,
        IsAdminOrReadOnly,
    )

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        token = 'Token {}'.format(request.auth)
        response['Authorization'] = token
        return response

class DepartmentRUDView(RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    # RetrieveUpdateDestroyAPIView put methodu override ediliyor(permission amacli)
    def put(self, request, *args, **kwargs):
        if self.request.user.is_superuser or self.request.user.is_staff:
            return self.update(request, *args, **kwargs)
        data = {
            'message' : 'You are not authorized to update!'
        }
        return Response(data, status=status.HTTP_401_UNAUTHORIZED)
    
    # RetrieveUpdateDestroyAPIView'in inherit aldigi DestroyModelMixin'in destroy methodu override ediliyor(permission amacli)
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if self.request.user.is_superuser:
            # self.perform_destroy(instance)
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        data = {
            'message' : 'You are not authorized to update!'
        }
        return Response(data, status=status.HTTP_401_UNAUTHORIZED)

class PersonnelListCreateView(ListCreateAPIView):
    queryset = Personnel.objects.all()
    serializer_class = PersonnelSerializer
    permission_classes = (
        IsAuthenticated,
        IsAdminOrReadOnly,
    )

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        token = 'Token {}'.format(request.auth)
        response['Authorization'] = token
        return response

class PersonnelRUDView(RetrieveUpdateDestroyAPIView):
    queryset = Personnel.objects.all()
    serializer_class = PersonnelSerializer

    # RetrieveUpdateDestroyAPIView put methodu override ediliyor(permission amacli)
    def put(self, request, *args, **kwargs):
        if self.request.user.is_superuser or self.request.user.is_staff:
            return self.update(request, *args, **kwargs)
        data = {
            'message' : 'You are not authorized to update!'
        }
        return Response(data, status=status.HTTP_401_UNAUTHORIZED)

    # RetrieveUpdateDestroyAPIView delete methodu override ediliyor(permission amacli)
    # def delete(self, request, *args, **kwargs):
    #     return self.destroy(request, *args, **kwargs)
    
    # RetrieveUpdateDestroyAPIView'in inherit aldigi DestroyModelMixin'in destroy methodu override ediliyor(permission amacli)
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if self.request.user.is_superuser:
            # self.perform_destroy(instance)
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        data = {
            'message' : 'You are not authorized to update!'
        }
        return Response(data, status=status.HTTP_401_UNAUTHORIZED)

    # def perform_destroy(self, instance):
    #     instance.delete()

class DepartmentPersonnelView(ListAPIView):
    # queryset = Department.objects.all()
    serializer_class = DepartmentPersonnelSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given one,
        by filtering against a `department` query parameter in the URL.
        """
        queryset = Department.objects.all()
        department = self.kwargs['department']
        if department is not None:
            return Department.objects.filter(name__iexact=department)