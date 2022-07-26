from django.shortcuts import render
from django.http import JsonResponse, response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from .models import TestModel
from django.forms.models import model_to_dict


class simple(APIView):

    def post(self, request):
        new_test_content = TestModel.objects.create(
            name=request.data["name"],
            description=request.data["description"],
            phone_number=request.data["phone_number"],
            is_alive=request.data["is_alive"],
            amount=request.data["amount"]
        )
        return JsonResponse({"data": model_to_dict(new_test_content)})

    def get(self, request):
        content = TestModel.objects.all().values()
        return JsonResponse({"data": list(content)})

# @csrf_exempt
# def json(request):
#     method = request.method.lower()
#     if method == "get":
#         return JsonResponse({"data": [1, 3, 4, 6, 5 , 6]})
#     elif method == "post":
#         return JsonResponse({"data": "added data suc"})
#     elif method == "put":
#         return JsonResponse({"data": "Updated data suc"})
#     return JsonResponse({"error": "Method " + request.method + " is not allowed"})
