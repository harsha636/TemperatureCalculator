from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    result = None

    if request.method == 'POST':
        temp = float(request.POST['temperature'])
        unit = request.POST['unit']

        result = f'Temperature in Fahrenheit {temp} is {temp * 9/5 + 32}' if unit == 'celsius' else f'Temperature in Celsius { temp } is {(temp - 32) * 5/9}'
        
    return render(request, 'home.html', {'result': result})