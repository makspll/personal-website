
## Wagtail
INSTALLED_APPS = INSTALLED_APPS + [
    'wagtail.contrib.forms',
    'wagtail.contrib.redirects',
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    'wagtail.admin',
    'wagtail.core',

    'modelcluster',
    'taggit',]

MIDDLEWARE = MIDDLEWARE + ['wagtail.contrib.redirects.middleware.RedirectMiddleware',]

WAGTAIL_SITE_NAME = 'mozolewskimaks.co.uk'

## wagtail-metadata

INSTALLED_APPS = INSTALLED_APPS + [
    'wagtailmetadata',
]

## wagtail-blocks
INSTALLED_APPS = INSTALLED_APPS +[
    'wagtailfontawesome',
    'wagtail_blocks',
]

##django-tz-detect
INSTALLED_APPS = INSTALLED_APPS +[
        'tz_detect',
]

MIDDLEWARE = MIDDLEWARE + ['tz_detect.middleware.TimezoneMiddleware',]
## custom apps

INSTALLED_APPS = INSTALLED_APPS + ['website']



## x-frame-options
# allow embeding own content on site
X_FRAME_OPTIONS = 'SAMEORIGIN'
