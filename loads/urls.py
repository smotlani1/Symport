from posixpath import basename
from django.urls import path, include
from . import views
from rest_framework_nested import routers

# Mapping URLs to views

router = routers.SimpleRouter()
router.register('viewloads', views.ViewLoadViewSet, basename='load')
loads_router = routers.NestedSimpleRouter(router, 'viewloads', lookup="load")
loads_router.register('uploads', views.LoadImageViewSet, basename="loadimage")

urlpatterns = [
    path(r'', include(router.urls)),
    path(r'', include(loads_router.urls)),
   
    
    
]