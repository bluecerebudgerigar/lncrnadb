import os
gettext = lambda s: s
PROJECT_PATH = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]
#django settings for production

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'lncrnadb',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': 'localhost',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
   
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True



MEDIA_ROOT = os.path.join(PROJECT_PATH, "media")
MEDIA_URL = "/media/"

STATIC_ROOT = os.path.join(PROJECT_PATH, "static")
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (  
    # Don't forget to use absolute paths, not relative paths.
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.DefaultStorageFinder',
 
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '80@xu=(j$$q0w=5mn@8=-qr1kpfo@tnjc^^bri+b+%2kihzeo2'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.middleware.common.CommonMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
)

ROOT_URLCONF = 'lncrnadb_deployment.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'lncrnadb_deployment.wsgi.application'

TEMPLATE_DIRS = (
    # The docs say it should be absolute path: PROJECT_PATH is precisely one.
    # Life is wonderful!
    os.path.join(PROJECT_PATH, "templates"),
    os.path.join(PROJECT_PATH, "djangolncrna_table"),
    os.path.join(PROJECT_PATH, "expression_django"),
    os.path.join(PROJECT_PATH, "lncrnadb_table"),   
)


CMS_TEMPLATES = (
    ('template_1.html', 'Template One'),
    ('template_2.html', 'Template Two'),
    ('template_3.html', 'Template Three'),
    ('home_template.html', 'Template Home'),
    ('auto_complete.html', 'AutoComplete'),
    ('entry_template.html', 'Entry Template'),
    ('search/search.html', 'search Template'),
    
)

INSTALLED_APPS = (
    #'djangocms_text_ckeditor',
    'cms',
    'cms_search',
    'cms.plugins',
    'tinymce',
    'haystack',
    'lncrnadbtable',
    'mptt',
    'menus',
    'south',
    'sekizai',   
    #'dajax',
    #}'dajaxice',
    'djangocms_table',
    'form_designer.contrib.cms_plugins.form_designer_form',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cms.plugins.file',
    'cms.plugins.flash',
    'cms.plugins.googlemap',
    'cms.plugins.link',
    'cms.plugins.picture',
    'cms.plugins.snippet',
    'cms.plugins.teaser',
    'cms.plugins.text',
    'cms.plugins.video',
    'cms.plugins.twitter',
    # Uncomment the next line to enable the admin:
     'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
     'django.contrib.admindocs',
)



SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}



HAYSTACK_SITECONF = 'simpleplug.search_sites'
HAYSTACK_SEARCH_ENGINE = 'whoosh'
HAYSTACK_WHOOSH_PATH= os.path.join(PROJECT_PATH, "whoosh_index")

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'cms.context_processors.media',
    'sekizai.context_processors.sekizai',
    'django.core.context_processors.debug',
    'django.contrib.messages.context_processors.messages' # !!!!!!!!!!!
    
    
)


CMS_PLACEHOLDER_CONF = {
    'content': {
        'plugins': ['TextPlugin', 'PicturePlugin'],
        'text_only_plugins': ['LinkPlugin'],
        'extra_context': {"width":640},
        'name':gettext("Content"),
    },
    'right-column': {
        "plugins": ['TeaserPlugin', 'LinkPlugin'],
        "extra_context": {"width":280},
        'name':gettext("Right Column"),
        'limits': {
            'global': 2,
            'TeaserPlugin': 1,
            'LinkPlugin': 1,
        },
    },
    'base.html content': {
        "plugins": ['TextPlugin', 'PicturePlugin', 'TeaserPlugin']
    },
}
CMS_USE_TINYMCE = True

#
#TINYMCE_DEFAULT_CONFIG = {
#    'theme' : 'advanced',
#    'theme_advanced_buttons1' :'bold,italic,underline,separator,bullist,numlist,separator,link,unlink,image,forecolor, fontsizeselect, table',
#    'theme_advanced_buttons2' : '',
#    'theme_advanced_buttons3' : '',
#    'theme_advanced_toolbar_location' : 'top',
#    'theme_advanced_toolbar_align': 'left',
#    'plugins': 'table',
#    'tools': 'inserttable',
#    'paste_text_sticky': True,
#    'paste_text_sticky_default' : True,
#    'valid_styles' : 'font-weight,font-style,text-decoration',
#     'valid_children' : "+body[style],-body[div],p[strong|a|#text]",
#
#}
TINYMCE_JS_URL = '/static/tiny_mce/tiny_mce.js'
TINYMCE_JS_ROOT = '/static/tiny_mce/tiny_mce.js'


    
TINYMCE_DEFAULT_CONFIG = {
    'theme' : 'advanced',
    'theme_advanced_buttons1' :'bold,italic,underline,separator,bullist,numlist,separator,link,unlink,image,forecolor, fontsizeselect, table,code, fontstyle',
    'theme_advanced_resizing' : True,
    'plugins': 'table',
    'tools' : 'inserttable'
}


CMS_PLACEHOLDER_CONF = {
    
    'NomenclaturePlugin' : {
        "plugins" : ['NomenclaturePlugin']
    },
    'AssociatedcompPlugin' : {
        "plugins" : ['AssociatedcompPlugin']
    },
    
    'SequencesPlugin' : {
        "plugins" : ['SequencesPlugin']
    },
        
    'ExpressionPlugin': {
        "plugins": ['ExpressionPlugin']
    },
    'SpeciesPlugin' : {
        "plugins": ['SpeciesPlugin']
    },
    'AnnotationPlugin': {
        "plugins": ['AnnotationPlugin']
    },
    'LiteraturePlugin' : {
        "plugins": ['LiteraturePlugin']
    }
}
