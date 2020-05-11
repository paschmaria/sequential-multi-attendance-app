from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt 
def whatsapp_bot(request):
    print(request.POST)

"""
Create booking:
- 
"""