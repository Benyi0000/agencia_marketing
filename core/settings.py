import os
import environ

env = environ.Env()
environ.Env.read_env()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = env.bool("DEBUG", default=False)

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS_DEV')

# ---- Apps ----
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
PROJECT_APPS = []
THIRD_PARTY_APPS = [
    'corsheaders',
    'rest_framework',
    'ckeditor',
    'ckeditor_uploader',
]
INSTALLED_APPS = DJANGO_APPS + PROJECT_APPS + THIRD_PARTY_APPS

# ---- CKEditor ----
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['Link', 'Unlink'],
            ['RemoveFormat', 'Source']
        ],
        'autoParagraph': False,
    }
}
CKEDITOR_UPLOAD_PATH = "media/"

# ---- Middleware ----
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    # 'whitenoise.middleware.WhiteNoiseMiddleware',  # <-- si quieres servir estáticos sin Nginx
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

# ---- Frontend (dist) ----
FRONTEND_DIST = os.path.join(BASE_DIR, "dist")

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [FRONTEND_DIST],   # Django va a servir dist/index.html
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

WSGI_APPLICATION = 'core.wsgi.application'

# ---- Database ----
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# ---- Password validation ----
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ---- Internacionalización ----
LANGUAGE_CODE = 'es'
TIME_ZONE = 'America/Bogota'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# ---- Static & Media ----
STATIC_URL = '/static/'

# destino de collectstatic → separado de tu carpeta frontend
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Django debe encontrar los assets que Vite genera en dist/assets
STATICFILES_DIRS = [ os.path.join(BASE_DIR, 'dist') ]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ---- DRF ----
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ]
}

# ---- CORS / CSRF ----
CORS_ALLOWED_ORIGINS = env.list('CORS_ORIGIN_WHITELIST_DEV')
CSRF_TRUSTED_ORIGINS = env.list('CSRF_TRUSTED_ORIGINS_DEV')

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# ---- Ajustes de producción ----
if not DEBUG:
    ALLOWED_HOSTS = env.list('ALLOWED_HOSTS_DEPLOY')
    CORS_ALLOWED_ORIGINS = env.list('CORS_ORIGIN_WHITELIST_DEPLOY')
    CSRF_TRUSTED_ORIGINS = env.list('CSRF_TRUSTED_ORIGINS_DEPLOY')

    DATABASES = {
        "default": env.db("DATABASES_URL"),
    }
    DATABASES["default"]["ATOMIC_REQUESTS"] = True
