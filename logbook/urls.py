from django.urls import path, include
from rest_framework_nested import routers
from . import views

router = routers.SimpleRouter()
router.register('', views.LogbookEntryViewSet, basename='logbook-entries')

urlpatterns = [
    path(r'', include(router.urls)),
    
   
    
    
]