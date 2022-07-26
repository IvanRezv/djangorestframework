from django.shortcuts import render
from django.http import JsonResponse, response
from django.views.decorators.csrf import csrf_exempt


def simple(request):
    a = 30 + 50
    return response.HttpResponse(f"<h1>{a}<h1>")


@csrf_exempt
def json(request):
    method = request.method.lower()
    if method == "get":
        return JsonResponse({"data": [1, 3, 4, 6, 5 , 6]})
    elif method == "post":
        return JsonResponse({"data": "added data suc"})
    elif method == "put":
        return JsonResponse({"data": "Updated data suc"})
    return JsonResponse({"error": "Method " + request.method + " is not allowed"})
