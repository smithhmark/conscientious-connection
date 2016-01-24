from django.shortcuts import render

from django.http import HttpResponse
from django.http import JsonResponse

data = {
    1: {"to": 1, "from": 0, "type":"email", "when":"2016010112"},
    2: {"to": 0, "from": 1, "type":"email", "when":"2016010113"},
    3: {"to": 1, "from": 0, "type":"email", "when":"2016010114"},
    }

def index(request):
    return HttpResponse("silly")

def all_contacts(request):
    return JsonResponse(data)

def contact(request, contact_id):
    return JsonResponse(data[int(contact_id)])
