import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings
from rest_framework import status

# ======================================================================================================================

API_KEY = settings.OPENWEATHER_API_KEY


class WeatherAPIView(APIView):
    """
    GET /weather/weather/?city=CityName
    برمی‌گرداند پیش‌بینی ۵ روزه برای شهر داده شده
    """

    def get(self, request, format=None):
        city = request.query_params.get('city')
        if not city:
            return Response({"error": "City parameter is required"}, status=status.HTTP_400_BAD_REQUEST)

        # فراخوانی OpenWeatherMap 5-day forecast
        url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&units=metric&appid={API_KEY}"
        res = requests.get(url)

        if res.status_code != 200:
            return Response({"error": "City not found or API error"}, status=res.status_code)

        data = res.json()

        # انتخاب ۵ روز (ساعت ۱۲:۰۰)
        days = []
        seen_dates = set()
        for item in data['list']:
            date_str = item['dt_txt'].split(' ')[0]
            if date_str not in seen_dates and item['dt_txt'].split(' ')[1] == "12:00:00":
                days.append({
                    "date": item['dt_txt'],
                    "temp": item['main']['temp'],  # سانتی‌گراد
                    "weather_desc": item['weather'][0]['description'],
                    "icon": item['weather'][0]['icon']
                })
                seen_dates.add(date_str)
            if len(days) == 5:
                break

        return Response({"city": city, "days": days}, status=status.HTTP_200_OK)

# ======================================================================================================================
