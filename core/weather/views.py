import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings
from rest_framework import status

# ======================================================================================================================
API_KEY = settings.OPENWEATHER_API_KEY  # کلید API از تنظیمات Django


# ======================================================================================================================
class WeatherAPIView(APIView):
    def get(self, request, format=None):
        # دریافت پارامتر city از query params
        city = request.query_params.get("city")
        if not city:
            # اگر city ارسال نشده بود، پاسخ خطا با کد 400 برگردان
            return Response(
                {"error": "City parameter is required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # ساخت URL برای فراخوانی OpenWeatherMap 5-day forecast
        url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&units=metric&appid={API_KEY}"
        res = requests.get(url)  # ارسال درخواست GET

        # بررسی وضعیت پاسخ
        if res.status_code != 200:
            # اگر درخواست موفق نبود، خطای مناسب بازگردان
            return Response(
                {"error": "City not found or API error"},
                status=res.status_code,
            )

        data = res.json()  # تبدیل پاسخ به JSON

        # ایجاد لیست روزها و جمع‌آوری اطلاعات هر روز
        days = []  # آرایه‌ای برای ذخیره پیش‌بینی روزانه
        seen_dates = set()  # برای جلوگیری از تکرار تاریخ‌ها

        for item in data.get("list", []):  # پیمایش لیست پیش‌بینی‌ها
            date_str, time_str = item["dt_txt"].split(
                " "
            )  # جدا کردن تاریخ و ساعت
            if date_str not in seen_dates and time_str == "12:00:00":
                # اگر تاریخ تکراری نبود و ساعت 12 ظهر بود، اطلاعات را اضافه کن
                days.append(
                    {
                        "date": item["dt_txt"],  # تاریخ و ساعت
                        "temp": item["main"]["temp"],  # دما بر حسب سانتی‌گراد
                        "weather_desc": item["weather"][0][
                            "description"
                        ],  # توضیح آب و هوا
                        "icon": item["weather"][0][
                            "icon"
                        ],  # آیکون وضعیت آب و هوا
                    }
                )
                seen_dates.add(
                    date_str
                )  # اضافه کردن تاریخ به set برای جلوگیری از تکرار

            if len(days) == 5:
                # اگر ۵ روز جمع شد، حلقه را متوقف کن
                break

        # ارسال پاسخ نهایی به صورت JSON شامل نام شهر و لیست روزها
        return Response(
            {"city": city, "days": days}, status=status.HTTP_200_OK
        )


# ======================================================================================================================
