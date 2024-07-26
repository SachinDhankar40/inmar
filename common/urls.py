from django.urls import path, include
from rest_framework_nested import routers
from .views import LocationViewSet, DepartmentViewSet, CategoryViewSet, SubCategoryViewSet, SKUViewSet

router = routers.DefaultRouter()
router.register('location', LocationViewSet, basename='location')
router.register('department', LocationViewSet, basename='department')
router.register('category', LocationViewSet, basename='category')
router.register('subcategory', LocationViewSet, basename='subcategory')
router.register('sku', SKUViewSet, basename='sku')

locations_router = routers.NestedDefaultRouter(router, 'location', lookup='location')
locations_router.register('department', DepartmentViewSet, basename='location')

departments_router = routers.NestedDefaultRouter(locations_router, 'department', lookup='department')
departments_router.register('category', CategoryViewSet, basename='department_category')

categories_router = routers.NestedDefaultRouter(departments_router, 'category', lookup='category')
categories_router.register('subcategory', SubCategoryViewSet, basename='category_subcategory')

subcategories_router = routers.NestedDefaultRouter(categories_router, 'subcategory', lookup='subcategory')
subcategories_router.register('sku', SKUViewSet, basename='sub_category_sku')

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/', include(locations_router.urls)),
    path('api/v1/', include(departments_router.urls)),
    path('api/v1/', include(categories_router.urls)),
    path('api/v1/', include(subcategories_router.urls))
]
