from pathlib import Path
import os
import dj_database_url

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
#   TIME & LANG
# ----------------------- #

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True




DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"

# Cloudinary credentials from environment variables
CLOUDINARY_STORAGE = {
    "CLOUD_NAME": os.environ.get("shop"),
    "API_KEY": os.environ.get("525535723275894"),
    "API_SECRET": os.environ.get("l7SGe7cpOszd82aK8h8AAxfGHBg"),
}

# ----------------------- #
#   STATIC FILES
# ----------------------- #

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# ----------------------- #
#   MEDIA FILES (S3)
# ----------------------- #

# Use S3 in production, fallback to local media in dev
if DEBUG:
    MEDIA_URL = '/media/'
    MEDIA_ROOT = BASE_DIR / 'media'
else:
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
    AWS_S3_REGION_NAME = os.getenv('AWS_S3_REGION_NAME', 'us-east-1')
    AWS_QUERYSTRING_AUTH = False
    MEDIA_URL = f'https://{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/'

# ----------------------- #
#   DEFAULT AUTOFIELD
# ----------------------- #

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
