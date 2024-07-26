from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Location, Department, Category, SubCategory, SKU
from .serializers import LocationSerializer, DepartmentSerializer, CategorySerializer, SubCategorySerializer, SKUSerializer

class LocationViewSet(viewsets.ModelViewSet):
    authentication_classes = ()
    permission_classes = ()
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class DepartmentViewSet(viewsets.ModelViewSet):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = DepartmentSerializer

    def get_queryset(self):
        params = {}
        if self.kwargs.get('location_pk'):
            params['location_id'] = self.kwargs.get('location_pk')
        return Department.objects.filter(location_id=self.kwargs['location_pk'])

class CategoryViewSet(viewsets.ModelViewSet):
    authentication_classes = ()
    permission_classes = ()
    
    serializer_class = CategorySerializer

    def get_queryset(self):
        params = {}
        if self.kwargs.get('department_pk'):
            params['department_id'] = self.kwargs.get('department_pk')
        return Category.objects.filter(department_id=self.kwargs['department_pk'])

class SubCategoryViewSet(viewsets.ModelViewSet):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = SubCategorySerializer

    def get_queryset(self):
        params = {}
        if self.kwargs.get('category_pk'):
            params['category_id'] = self.kwargs.get('category_pk')
        return SubCategory.objects.filter(category_id=self.kwargs['category_pk'])

class SKUViewSet(viewsets.ModelViewSet):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = SKUSerializer
    filterset_fields = {
        "name": ['exact'],
        "location": ['in', 'exact'],
        "department": ['in', 'exact'],
        "category": ['in', 'exact'],
        "subcategory": ['in', 'exact']
    }

    def get_queryset(self):
        params = {}
        if self.kwargs.get('subcategory_pk'):
            params['subcategory_id'] = self.kwargs.get('subcategory_pk')
        return SKU.objects.filter(**params)
