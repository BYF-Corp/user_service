from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.contrib.auth.models import User
from user_management.models import Customer, Employee
from user_management.serializers import CustomerSerializer, EmployeeSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

@csrf_exempt
def register(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        try:
            new_user = User.objects.create_user(username=data['username'], password=data['password'])
        except:
            return JsonResponse({"error": "username already used."}, status=400)
        new_user.save()
        data['user'] = new_user.id
        employee_serializer = EmployeeSerializer(data=data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse(employee_serializer.data, status=201)
        new_user.delete()
        return JsonResponse({"error": "data not valid"}, status=400)
    return JsonResponse({"error": "method not allowed."}, status=405)

class EmployeeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        employee_data = Employee.objects.get(user=request.user)
        employee_serializer = EmployeeSerializer(employee_data)
        content = {
            'data': employee_serializer.data
        }
        return Response(content)