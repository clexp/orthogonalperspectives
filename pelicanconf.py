AUTHOR = 'clexp'
SITENAME = 'Journey to ML'
SITEURL = ''


PATH = 'content'
STATIC_PATHS = ['images',
                'extras',
                'images/Literature',
                'images/Machine Learning']

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'
THEME = 'theme/gum'

  # clexp added
SITESUBTITLE = 'A Mechanical Engineer turned Medic, voyages through Maths and into Machine Learning'
DEFAULT_CATEGORY = 'other'

# Feed generation is usually not desired when developing
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = True
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

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
