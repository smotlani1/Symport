from django.urls import path, include
from . import views
from rest_framework_nested import routers


router = routers.SimpleRouter()


router.register('viewloads', views.ViewLoadViewSet, basename='viewloads')
loads_router = routers.NestedSimpleRouter(router, 'viewloads', lookup="load")
loads_router.register('uploads', views.LoadImageViewSet, basename="load-images")

urlpatterns = [
    path(r'', include(router.urls)),
    path(r'', include(loads_router.urls)),
    # path('viewloads/<id>', views.GetLoadDetails.as_view()),
    
    
]