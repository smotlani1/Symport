from django.contrib.auth.mixins import LoginRequiredMixin
from itertools import product
from django.shortcuts import get_list_or_404, get_object_or_404
from django.http import HttpResponse
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

# @method_decorator(login_required)
class ViewLoadViewSet(LoginRequiredMixin, GenericViewSet, RetrieveModelMixin, ListModelMixin):

    serializer_class = LoadSerializer

    def get_queryset(self):
        return Load.objects.filter(user_id=self.request.user)


class LoadImageViewSet(ModelViewSet):
    serializer_class = LoadImageSerializer
    
    def get_serializer_context(self):
        return {'load_id': self.kwargs['load_pk']}
    
    def get_queryset(self):
        return LoadImage.objects.filter(load_id=self.kwargs["load_pk"])


class LoadImageSecondaryViewSet(ModelViewSet):
    serializer_class = LoadImageSerializer
    
    def get_serializer_context(self):
        return {'load_id': self.kwargs['pk']}
    
    def get_queryset(self):
        return LoadImage.objects.filter(load_id=self.kwargs["pk"])



# class ViewLoads(APIView):
#     @method_decorator(login_required)
#     def get(self, request):
#         queryset = Load.objects.filter(user_id=request.user)
#         serializer = LoadSerializer(queryset, many=True)
#         return Response(serializer.data)



# class GetLoadDetails(APIView):
#     @method_decorator(login_required)
#     def get(self, request, id):
#         load = get_object_or_404(Load, pk=id)
#         serializer = LoadSerializer(load)
#         return Response(serializer.data)



# class LoadImageViewSet(APIView):
#     parser_classes = [FileUploadParser]

#     @method_decorator(login_required)
#     def get(self, request, id):
#         return Response("OK")
    

#     @method_decorator(login_required)
#     def put(self, request, id, filename, format=None):
#         # load = get_object_or_404(LoadImage, pk=id)
#         # serializer = LoadImageSerializer(load, data=request.data)
#         # serializer.is_valid(raise_exception=True)
#         # serializer.save()
#         # return Response(serializer.data)

#         file_obj = request.data['file']
#         return Response(status=204)

