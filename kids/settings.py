from pathlib import Path
import os
import dj_database_url
import cloudinary
import cloudinary.uploader
import cloudinary.api

# ----------------------- #
#   BASE DIRECTORY
# ----------------------- #
BASE_DIR = Path(__file__).resolve().parent.parent

# ----------------------- #
#   SECURITY & DEBUG
# ----------------------- #
SECRET_KEY = 'django-insecure-!your-secret-key-here!'
DEBUG = False
ALLOWED_HOSTS = ['*']

CSRF_TRUSTED_ORIGINS = [
    "https://kidsitemshop-production.up.railway.app",
]

# ----------------------- #
#   INSTALLED APPS
# ----------------------- #
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Your apps
    'shop',

    # S3 storage
    'storages',

    # Cloudinary
    "cloudinary",
    "cloudinary_storage",
]

# ----------------------- #
#   MIDDLEWARE
# ----------------------- #
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'kids.urls'

# ----------------------- #
#   TEMPLATES
# ----------------------- #
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

# ----------------------- #
#   DATABASES
# ----------------------- #
DATABASES = {
    'default': dj_database_url.config(
        default=f"sqlite:///{BASE_DIR}/db.sqlite3",
        conn_max_age=600
    )
}

# ----------------------- #
#   PASSWORD VALIDATION
# ----------------------- #
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ----------------------- #
#   TIME & LANGUAGE
# ----------------------- #
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ----------------------- #
#   STATIC FILES
# ----------------------- #
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# ----------------------- #
#   MEDIA FILES
# ----------------------- #
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# ----------------------- #
#   CLOUDINARY SETTINGS
# ----------------------- #
cloudinary.config(
    cloud_name="dlfr1kfqa",
    api_key="525535723275894",
    api_secret="l7SGe7cpOszd82aK8h8AAxfGHBg"
)

CLOUDINARY_STORAGE = {
    "CLOUD_NAME": "dlfr1kfqa",
    "API_KEY": "525535723275894",
    "API_SECRET": "l7SGe7cpOszd82aK8h8AAxfGHBg",
}

DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"

# ----------------------- #
#   DEFAULT AUTO FIELD
# ----------------------- #
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
