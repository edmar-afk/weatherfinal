from django.shortcuts import render
from .models import WeatherPrediction
import random
# Create your views here.

num = random.randint(1, 35)

def homepage(request):
    return render(request, 'homepage.html')
    
def predict_weather(request):
    history = WeatherPrediction.objects.all().order_by('-id')
    latest = WeatherPrediction.objects.latest('id')
    context = {'history' : history, 'latest' : latest}
    if request.method == 'POST':
        photo = request.FILES['photo']

        if num >= 5 and num <= 15:
            prediction = WeatherPrediction(photo=photo, temperature=num, condition='Rainy')
            prediction.save()
        
        elif num >= 16 and num <= 50:
            prediction = WeatherPrediction(photo=photo, temperature=num, condition='Sunny')
            prediction.save()
    
    return render(request, 'predict.html', context)