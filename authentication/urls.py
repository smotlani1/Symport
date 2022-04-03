from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]


# from rest_framework_simplejwt import views as jwt_views
# from .views import ObtainTokenPairWithColorView


# urlpatterns = [
#     path('token/obtain/', ObtainTokenPairWithColorView.as_view(), name='token_create'),  
#     path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
# ]