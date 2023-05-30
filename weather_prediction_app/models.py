from django.db import models
from django.core.validators import FileExtensionValidator
from django.db import models
from datetime import datetime
from django.utils import timezone
# Create your models here.

now = timezone.now()

class WeatherPrediction(models.Model):
    photo = models.ImageField(upload_to='photos/', validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])],)
    date = models.DateField(default=now)
    temperature = models.FloatField(max_length=100)
    condition = models.CharField(max_length=100)

    def __str__(self):
        return f'Temperature: {self.temperature}°C, Condition: {self.condition}'
