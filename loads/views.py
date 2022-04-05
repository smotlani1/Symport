from itertools import product
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.mixins import *
from rest_framework.viewsets import *
from rest_framework.response import Response
from rest_framework.parsers import FormParser, MultiPartParser, FileUploadParser
from .models import *
from .serializers import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Removed LoginRequiredMixin, 
class ViewLoadViewSet(GenericViewSet, RetrieveModelMixin, ListModelMixin):

    serializer_class = LoadSerializer
    # queryset = Load.objects.all()

    # Re enable below portion to require login, and filter by user. 
    def get_queryset(self):
        return Load.objects.filter(user=self.request.user) #Filtered to only show Users their own data, and not other users' data#


class LoadImageViewSet(ModelViewSet):
    serializer_class = LoadImageSerializer
    
    def get_serializer_context(self):
        return {'load_id': self.kwargs['load_pk']}
    
    def get_queryset(self):
        return LoadImage.objects.filter(load_id=self.kwargs["load_pk"])



