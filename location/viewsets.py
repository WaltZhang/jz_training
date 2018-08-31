from django.http import Http404
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status

from .models import Province, City, District
from .serializers import ProvinceSerializer, CitySerializer, DistrictSerializer


class ProvinceList(APIView):
    def get(self, request, format=None):
        provinces = Province.objects.all()
        serializer = ProvinceSerializer(provinces, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProvinceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProvinceCities(ListAPIView):
    serializer_class = CitySerializer

    def get_queryset(self):
        return City.objects.filter(province__code=self.kwargs['pcode'])


class CityList(APIView):
    def get(self, request, format=None):
        cities = City.objects.all()
        serializer = CitySerializer(cities, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CityDistricts(ListAPIView):
    serializer_class = DistrictSerializer

    def get_queryset(self):
        return District.objects.filter(city__code=self.kwargs['ccode'])


class DistrictList(APIView):
    def get(self, request, format=None):
        districts = District.objects.all()
        serializer = DistrictSerializer(districts, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DistrictSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
