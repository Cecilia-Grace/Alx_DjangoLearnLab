from django.shortcuts import render
from .models import Student, Unit
from rest_framework import viewsets
from .serializers import StudentSerializer, UnitSerializer

# Create your views here.
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    
class UnitViewSet(viewsets.ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    
