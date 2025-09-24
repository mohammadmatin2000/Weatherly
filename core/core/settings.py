from pathlib import Path  # مدیریت مسیرها
from decouple import config  # خواندن متغیرهای محیطی از فایل .env

# ======================================================================================================================
# مسیرهای پایه پروژه

BASE_DIR = Path(__file__).resolve().parent.parent  # مسیر دایرکتوری اصلی پروژه

# ======================================================================================================================
# تنظیمات سریع توسعه (برای production مناسب نیست)

SECRET_KEY = "django-insecure-buc1pi3l8qmuwpc)=@@q6_bw30j05-ap6x-cup8g=bp$!^udbj"  # کلید محرمانه پروژه
DEBUG = True  # حالت توسعه (برای تولید باید False شود)
ALLOWED_HOSTS = []  # دامنه‌های مجاز برای دسترسی به سرور

# ======================================================================================================================
# برنامه‌های نصب شده

INSTALLED_APPS = [
    "django.contrib.admin",  # پنل مدیریت
    "django.contrib.auth",  # سیستم احراز هویت
    "django.contrib.contenttypes",  # مدیریت مدل‌ها
    "django.contrib.sessions",  # مدیریت سشن‌ها
    "django.contrib.messages",  # پیام‌ها
    "django.contrib.staticfiles",  # مدیریت فایل‌های استاتیک
    "rest_framework",  # Django REST Framework
    "drf_yasg",  # مستندسازی API با Swagger
    "corsheaders",  # مدیریت CORS
    "weather",  # اپلیکیشن هواشناسی
]

# ======================================================================================================================
# Middlewareها

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",  # مدیریت CORS
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# ======================================================================================================================
# تنظیمات URL و Template

ROOT_URLCONF = "core.urls"  # فایل URL اصلی پروژه

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",  # موتور Template
        "DIRS": [BASE_DIR / "templates"],  # مسیر پوشه قالب‌ها
        "APP_DIRS": True,  # فعال کردن Templateهای اپ‌ها
        "OPTIONS": {
            "context_processors": [  # Context processor ها
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"  # فایل WSGI پروژه

# ======================================================================================================================
# تنظیمات دیتابیس

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",  # موتور PostgreSQL
        "NAME": config("PG_NAME", default="default_database"),  # نام دیتابیس
        "USER": config("PG_USER", default="username"),  # نام کاربری
        "PASSWORD": config("PG_PASSWORD", default="password"),  # پسورد
        "HOST": config("PG_HOST", default="db"),  # هاست دیتابیس
        "PORT": config("PG_PORT", cast=int, default=5432),  # پورت
    }
}

# ======================================================================================================================
# اعتبارسنجی پسورد

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# ======================================================================================================================
# بین المللی سازی

LANGUAGE_CODE = "en-us"  # زبان پروژه
TIME_ZONE = "UTC"  # منطقه زمانی
USE_I18N = True  # فعال بودن ترجمه
USE_TZ = True  # فعال بودن timezone-aware

# ======================================================================================================================
# فایل‌های استاتیک و رسانه
STATIC_URL = "/static/"  # URL فایل‌های استاتیک
STATIC_ROOT = BASE_DIR / "staticfiles"  # مسیر جمع‌آوری فایل‌های استاتیک
MEDIA_ROOT = BASE_DIR / "media"  # مسیر فایل‌های آپلود شده
MEDIA_URL = "/media/"  # URL فایل‌های رسانه‌ای
STATICFILES_DIRS = [BASE_DIR / "static"]  # مسیر فایل‌های استاتیک در پروژه
# ======================================================================================================================
# کلید پیش‌فرض مدل‌ها
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"  # نوع پیش‌فرض کلید اصلی
# ======================================================================================================================
# تنظیمات CORS
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  # اجازه دسترسی از فرانت React
]
CORS_ALLOW_ALL_ORIGINS = True  # اجازه همه منابع (در توسعه)
# ======================================================================================================================
# کلید API OpenWeatherMap
OPENWEATHER_API_KEY = (
    "72eb22b83816ad96b1f44854e8ee2ffd"  # کلید API برای گرفتن داده‌های هواشناسی
)
# ======================================================================================================================
