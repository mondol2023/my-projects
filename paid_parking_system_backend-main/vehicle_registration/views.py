from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from .models import VehicleRegistration  

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import VehicleRegistrationSerializer
from django.shortcuts import get_object_or_404

@csrf_exempt  
def vehicle_registration(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))

            vehicle_type = data.get('vehicle_type')
            vehicle_name = data.get('vehicle_name')
            vehicle_model = data.get('vehicle_model')
            vehicle_license = data.get('vehicle_license')
            vehicle_length = data.get('vehicle_length')
            vehicle_width = data.get('vehicle_width')
            vehicle_height = data.get('vehicle_height')
            driver_name = data.get('driver_name')
            driver_phone = data.get('driver_phone')
            driver_license = data.get('driver_license')
            owner_name = data.get('owner_name')
            owner_phone = data.get('owner_phone')

            
            VehicleRegistration.objects.create(
                vehicle_type=vehicle_type,
                vehicle_name=vehicle_name,
                vehicle_model=vehicle_model,
                vehicle_license=vehicle_license,
                vehicle_length=vehicle_length,
                vehicle_width=vehicle_width,
                vehicle_height=vehicle_height,
                driver_name=driver_name,
                driver_phone=driver_phone,
                driver_license=driver_license,
                owner_name=owner_name,
                owner_phone=owner_phone
            )

            return JsonResponse({
                'message': 'Vehicle registered successfully!',
                'data': data
            }, status=201)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

    return JsonResponse({'error': 'Only POST method is allowed'}, status=405)


class VehicleRegistrationAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                obj = VehicleRegistration.objects.get(pk=pk, is_active=True)
            except VehicleRegistration.MultipleObjectsReturned:
                return Response({'error': 'Multiple objects found'}, status=status.HTTP_400_BAD_REQUEST)
            except VehicleRegistration.DoesNotExist:
                return Response({'error': 'Object not found'}, status=status.HTTP_404_NOT_FOUND)
            
            serializer = VehicleRegistrationSerializer(obj)
            return Response(serializer.data)
        
        query_set = VehicleRegistration.objects.all().filter(is_active=True)
        serializer = VehicleRegistrationSerializer(query_set, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = VehicleRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)


    def put(self, request, pk):
        obj = get_object_or_404(VehicleRegistration, pk=pk)
        serializer = VehicleRegistrationSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk):
        obj = get_object_or_404(VehicleRegistration, pk=pk)
        obj.is_active = False
        obj.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
