from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def time_info(request):
    date=datetime.datetime.now()
    msg="<h1>Now the current time is: " +str(date)+"</h1>"
    return HttpResponse(msg)
