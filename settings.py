# Django settings for Ujima project.

DEBUG =True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
     ('moses', 'moses@appfrica.org'),
 ('Ron Nixon', 'moses@appfrica.org'),
)

MANAGERS = ADMINS
import os
import sys
UJIMA_ROOT = os.path.realpath(os.path.dirname(__file__))
DATABASE_ENGINE = 'mysql'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = 'ujimaproject66'             # Or path to database file if using sqlite3.
DATABASE_USER = 'root'             # Not used with sqlite3.
DATABASE_PASSWORD = 'mosespass'         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.
TEMPLATES = os.path.join(UJIMA_ROOT,'templates')
BLOG_TEMPLATES=os.path.join(UJIMA_ROOT,'blog/templates')
MEDIA_PATH=os.path.join(UJIMA_ROOT,'Media')
# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'
SEARCH_STORAGE_PATH = os.path.join(UJIMA_ROOT,'db_index')
SEARCH_STORAGE_TYPE = "fs"
# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"

MEDIA_ROOT = os.path.join(UJIMA_ROOT,'Media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/Media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'yf@s4#90--3j$$qxiu%^0xt+wxmc_+#b(5=u7e-@oos^z%&j3j'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
    
)

MIDDLEWARE_CLASSES = (
   # 'search.middleware.LuceneMiddleware',                  
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'pagination.middleware.PaginationMiddleware',
    'django.middleware.doc.XViewMiddleware',
)

ROOT_URLCONF = 'Ujima.urls'

TEMPLATE_CONTEXT_PROCESSORS=(
 'django.core.context_processors.request',
 'django.core.context_processors.auth',
 )

TEMPLATE_DIRS = (
                 TEMPLATES,
                 BLOG_TEMPLATES,
    
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
     'django.contrib.sites',
    'django.contrib.admin',
     'django.contrib.markup',
    'django.contrib.comments',
    'django.contrib.sessions',
    'django.contrib.sites',
    'Ujima.globalfund',
    'Ujima.lobby',
    'Ujima.basic.blog',
    'Ujima.basic.inlines',
    'Ujima.docshare',
    'tagging',
    'pagination',
    'Ujima.usaid.aid',
    'Ujima.weapons.arms',
    'Ujima.main',
    'djangosphinx2',
    'Ujima.dfid.ukaid',
    'mapping',
    'django.contrib.gis',
    #'world',
 
 'Ujima.afJuma.afdb',

    
)
API_KEY="62l4lblxiwijoz6sm76ih"

API_SECRET="sec-3cwsy77p09nsqv2dzgatdrb17h"
SPHINX_API_VERSION = 0x113
map_production_key="ABQIAAAAYimH_excdTjwGjM6LcP-DhTFy5CdpwgrbtEYhW0ROWO43JYeTBRtMrlpB-kqfHssovWAOVFKpzM6sQ"
map_development_key="ABQIAAAAYimH_excdTjwGjM6LcP-DhTPPuSUNeBR8jm1dVT7TVbcdz8N0RTpWwi1zOMJcL1W9U44GCX4NeiAGw"
