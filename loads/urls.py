from posixpath import basename
from django.urls import path, include
from . import views
from rest_framework_nested import routers

# loadimagerouter = routers.SimpleRouter()
# loadimagerouter.register('loadimages', views.LoadImageSecondaryViewSet, basename='loadimage')

router = routers.SimpleRouter()
router.register('viewloads', views.ViewLoadViewSet, basename='load')
loads_router = routers.NestedSimpleRouter(router, 'viewloads', lookup="load")
loads_router.register('uploads', views.LoadImageViewSet, basename="loadimage")

urlpatterns = [
    path(r'', include(router.urls)),
    path(r'', include(loads_router.urls)),
    # path(r'', include(loadimagerouter.urls)),
    # path('viewloads/<id>', views.GetLoadDetails.as_view()),
    
    
]