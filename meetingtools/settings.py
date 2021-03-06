# Django settings for meetingtools project.
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS

import meetingtools.site_logging
import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

SRC_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.abspath(os.path.join(SRC_DIR, '..'))

MANAGERS = ADMINS

LOCK_DIR = "/var/lock"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '%s/db/sqlite.db' % BASE_DIR,                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

GRACE = 10
IMPORT_TTL = 30
DEFAULT_TEMPLATE_SCO=18807
APPEND_SLASH = False

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Stockholm'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True
USE_TZ = True

STATIC_ROOT = "%s/static" % BASE_DIR
STATIC_URL = "/static/"

LOGIN_URL = "/accounts/login"
LOGOUT_URL = "/accounts/logout"
DEFAULT_URL = "/"

# Make this unique, and don't share it with anybody.
SECRET_KEY = ''

SESSION_ENGINE = "django.contrib.sessions.backends.file"
#SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_FILE_PATH = "/tmp"
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_COOKIE_AGE=36000

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake'
    }
}

THEMES = {
    '__default__': {'base': "%s/themes/default" % STATIC_URL },
    'meetingtools.nordu.net': {'base': "%s/themes/meetingtools.nordu.net" % STATIC_URL}
}

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'meetingtools.urlmiddleware.UrlMiddleware',
    'meetingtools.django-crossdomainxhr-middleware.XsSharing',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    #'django.contrib.auth.middleware.RemoteUserMiddleware'
)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.RemoteUserBackend',
    'django.contrib.auth.backends.ModelBackend',
)

ROOT_URLCONF = 'meetingtools.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    "%s/templates" % BASE_DIR
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.humanize',
    'django_extensions',
    'south',
    'django_co_connector',
    'django_co_acls',
    'tagging',
    'djangosaml2',
    'meetingtools.extensions',
    'meetingtools.apps.auth',
    'meetingtools.apps.room',
    'meetingtools.apps.cluster',
    'meetingtools.apps.userprofile',
    'meetingtools.apps.stats',
    'meetingtools.apps.sco',
    'meetingtools.apps.archive',
    'meetingtools.apps.content'
)

CARROT_BACKEND = "django"

NOREPLY = "no-reply@sunet.se"
AUTH_PROFILE_MODULE = "userprofile.UserProfile"

LOGIN_URL = '/saml2/sp/login/'
LOGIN_REDIRECT_URL = "/rooms"

POST_LOGOUT = '/Shibboleth.sso/Logout'

AUTO_REMOTE_SUPERUSERS = ['leifj@nordu.net']

#try:
#    from asgard.loader import *
#    DEBUG=True
#
#    AUTHENTICATION_BACKENDS += ('asgard.saml.Saml2Backend',)
#except ImportError,ex:
#    print ex
