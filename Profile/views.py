
from rest_framework.response import Response

from django.shortcuts import get_object_or_404
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from Profile.models import Example3
from Profile.models import CiudadM
from Profile.models import GeneroM
from Profile.models import OcupacionM
from Profile.models import EstadoM
from Profile.models import Estado_civilM


from Profile.serializer import Example3
from Profile.serializer import CiudadS
from Profile.serializer import GeneroS
from Profile.serializer import OcupacionS
from Profile.serializer import EstadoS
from Profile.serializer import Estado_civilS



from Profile.serializer import Example3Serializers



class ExampleList3(APIView):
    #METODO GET PARA SOLICITAR INFO
    def get (self , request , format = None):
        print("Metodo get filter")
        queryset = Example3.objects.filter(delete = False)
        #many true si se aplica retornos multiples objetos
        serializer = Example3Serializers(queryset, many= True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = Example3Serializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)





class CiudadList(APIView):
    def get (self , request , format = None):
        print("Metodo get filter")
        queryset = CiudadM.objects.filter(delete = False)
        #many true si se aplica retornos multiples objetos
        serializer = CiudadS(queryset, many= True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CiudadS(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class GeneroList(APIView):
    def get (self , request , format = None):
        print("Metodo get filter")
        queryset = GeneroM.objects.filter(delete = False)
        #many true si se aplica retornos multiples objetos
        serializer = GeneroS(queryset, many= True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = GeneroS(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class OcupacionList(APIView):
    def get (self , request , format = None):
        print("Metodo get filter")
        queryset = OcupacionM.objects.filter(delete = False)
        #many true si se aplica retornos multiples objetos
        serializer = OcupacionS(queryset, many= True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = OcupacionS(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class EstadoList(APIView):
    def get (self , request , format = None):
        print("Metodo get filter")
        queryset = EstadoM.objects.filter(delete = False)
        #many true si se aplica retornos multiples objetos
        serializer = EstadoS(queryset, many= True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EstadoS(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class Estado_civilList(APIView):
    def get (self , request , format = None):
        print("Metodo get filter")
        queryset = Estado_civilM.objects.filter(delete = False)
        #many true si se aplica retornos multiples objetos
        serializer = Estado_civilS(queryset, many= True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = Estado_civilS(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

        