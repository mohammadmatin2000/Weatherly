import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings
# ======================================================================================================================
class WeatherAPIView(APIView):
    def post(self, request):
        city = request.data.get('city')  # برای form-urlencoded هم جواب میده
        if not city:
            return Response({'error': 'City is required'}, status=400)

        api_key = settings.OPENWEATHER_API_KEY
        print(api_key)

        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        response = requests.get(url)
        data = response.json()
        return Response(data)
# ======================================================================================================================