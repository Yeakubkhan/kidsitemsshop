from pathlib import Path
import dj_database_url
import cloudinary.uploader
import cloudinary.api



BASE_DIR = Path(__file__).resolve().parent.parent

# ---------------------------
# SECURITY
# ---------------------------
SECRET_KEY = "django-insecure-key"
DEBUG = False

ALLOWED_HOSTS = ['kidsitemsshop.pythonanywhere.com']

CSRF_TRUSTED_ORIGINS = ['https://kidsitemsshop.pythonanywhere.com']



# ---------------------------
# INSTALLED APPS
# ---------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'shop',
    'cloudinary',
    'cloudinary_storage',

]

# ---------------------------
# MIDDLEWARE
# ---------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

ROOT_URLCONF = 'kids.urls'

# ---------------------------
# TEMPLATES
# ---------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'kids.wsgi.application'

# ---------------------------
# DATABASE
# ---------------------------
DATABASES = {
    'default': dj_database_url.config(
        default=f"sqlite:///{BASE_DIR}/db.sqlite3",
        conn_max_age=600
    )
}

# ---------------------------
# STATIC FILES
# ---------------------------
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'



MEDIA_URL = "/media/"

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'dlfr1kfqa',
    'API_KEY': '798444638744245',
    'API_SECRET': 'uoiNU8bdvL6lvRW5_Pu4QeIkyLM'
}
DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"
# ---------------------------
# DEFAULT AUTO FIELD
# ---------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

import cloudinary
cloudinary.config(
    cloud_name="dlfr1kfqa",
    api_key="798444638744245",
    api_secret="uoiNU8bdvL6lvRW5_Pu4QeIkyLM"
)
