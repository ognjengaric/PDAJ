from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Calculation
from .serializers import CalculationSerializer, InfoSerializer
from .calculations.calculations import *


def helper(request, method):
    serializer = InfoSerializer(data=request.data)
    if serializer.is_valid():
        data = serializer.validated_data
        result, time_in_s, max_memory_in_MB = calculate(data["n"], data["m"], data["points"], method)

        calc = Calculation(result, time_in_s, max_memory_in_MB)
        ser = CalculationSerializer(calc)
        return Response(ser.data)

    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class Sequential(APIView):

    def post(self, request):
        return helper(request, "s")


class Comprehension(APIView):

    def post(self, request):
        return helper(request, "c")


class Generators(APIView):

    def post(self, request):
        return helper(request, "g")


class Multiprocessing(APIView):

    def post(self, request):
        return helper(request, "m")
