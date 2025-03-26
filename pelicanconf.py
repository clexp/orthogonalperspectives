AUTHOR = 'clexp'
SITENAME = 'Journey to ML'
SITEURL = ''

# Enable live reload
LIVERELOAD = True
LIVERELOAD_HOST = 'localhost'
LIVERELOAD_PORT = 35729

PATH = 'content'
STATIC_PATHS = ['images']

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'
THEME = 'theme/gum'

  # clexp added
SITESUBTITLE = 'A Mechanical Engineer turned Medic, voyages through Maths and into Machine Learning'
# DEFAULT_CATEGORY = 'Machine Learning'
USE_FOLDER_AS_CATEGORY = True
MENUITEMS = (
    ('Home', '/'),
    ('About', '/pages/about.html'),
    ('Contact', '/pages/contact.html'),
    ('Site Notes', '/pages/site-notes.html')
)

# Feed generation is usually not desired when developing
# in the base.html, both of the next two 'DISPLAY..' params are inverted
# and a 'menu' is a nav bar
DISPLAY_PAGES_ON_MENU = False # False is DO put static pages in nav
DISPLAY_CATEGORIES_ON_MENU = True # True is DONT put categories in nav
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# clexp added
#  menuitems are really pre-nav items
# MENUITEMS = (('oh, this', 'https://shop.pimoroni.com/'),
#          ('and that', 'https://thepihut.com/'),)

# Blogroll
LINKS = (('My ML/AI Blog', 'https://www.linkedin.com/?original_referer='),
         ('Who I am?', 'https://www.facebook.com/'),
         ('General blog', 'https://twitter.com/'),
         ('Book reviews', 'https://www.amazon.co.uk/'),)

# Social widget
SOCIAL = (('Facebook', 'https://shop.pimoroni.com/'),
          ('Linked in', 'https://thepihut.com/'),)

DEFAULT_PAGINATION = 7

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
