AUTHOR = 'EasyDevMixin'
SITENAME = 'Easy Resources for Developers'
SITEURL = ""

PATH = "content"

TIMEZONE = 'UTC'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

CUSTOM_JS = 'static/js/custom.js'
STATIC_PATHS = ['img', 'js']
EXTRA_PATH_METADATA = {
    'js/custom.js': {'path': 'static/js/custom.js'}
}

# Blogroll
LINKS = (
    # ("Pelican", "https://getpelican.com/"),
    # ("Python.org", "https://www.python.org/"),
    # ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    # ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ('github', 'https://github.com/easydevmixin'),
    ('linkedin', 'https://es.linkedin.com/in/ramagaes/'),
)

LOAD_CONTENT_CACHE = False

DEFAULT_METADATA = {
    'status': 'draft',
}

SITEICON = "theme/images/logo-2-lines-200.png"
HEADER = "theme/images/logo-2-lines-200.png"

DEFAULT_PAGINATION = 10

# Themes
THEME = 'theme'
# BOOTSTRAP_THEME = 'united'

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

PLUGIN_PATHS = ["plugins", ]
PLUGINS = ['i18n_subsites', 'tag_cloud', ]

# mapping: language_code -> settings_overrides_dict
I18N_SUBSITES = {
    'ca': {
        'SITENAME': 'EasyDevMixin en Català',
    },
}

# Formatting for urls

ARTICLE_URL = "posts/{date:%Y}/{date:%m}/{slug}/"
ARTICLE_SAVE_AS = "posts/{date:%Y}/{date:%m}/{slug}/index.html"

CATEGORY_URL = "category/{slug}"
CATEGORY_SAVE_AS = "category/{slug}/index.html"

TAG_URL = "tag/{slug}/"
TAG_SAVE_AS = "tag/{slug}/index.html"

# Generate yearly archive

YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'

# Show most recent posts first

NEWEST_FIRST_ARCHIVES = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
