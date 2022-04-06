from django.shortcuts import render
import requests

def home(request):
    return render(request, 'pals/APIHome.html')

def profile(request):
    return render(request, 'pals/APIProfile.html')

def stats(request):
    return render(request, 'pals/APIStatistics.html')

def routes(request):
    return render(request, 'pals/APIRoutes.html')

def traffic(request):
    return render(request, 'pals/APITraffic.html')

def lgs(request):
    return render(request, 'pals/APILGS.html')