#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Siddhant Shrivastava'
SITENAME = u'sidcode'
SITETITLE = u'sidcode'
SITEURL = 'https://sidcode.github.io'

PATH = 'content'

TIMEZONE = 'Asia/Singapore'
DEFAULT_DATE_FORMAT = '%B %d, %Y'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Uncomment these to test the feeds
FEED_DOMAIN = 'https://sidcode.github.io'
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

DEFAULT_PAGINATION = 2

PAGINATION_PATTERNS = (
    (1, '{url}', '{save_as}'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# My own defaults
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.sane_lists': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.smarty': {},
    },
    'output_format': 'html5',
}

PLUGIN_PATHS = ['plugins']
# SID EDIT: Remove yuicompressor, later replace with webdepcompressor
PLUGINS = ['wip_extensions', 'neighbors', 'sitemap', 'simple_footnotes', 'render_math', 'liquid_tags', 'more_categories']
LIQUID_TAGS = ["img", "literal", "video", "youtube", "vimeo", "include_code"]

#SID EDIT: https://github.com/pelican-plugins/render-math Explore everything here, does not seem to work
#MATH_JAX = {'tex_extensions': ['color.js','mhchem.js'], 'color':'blue','align':'left'}

THEME = 'theme'
LOGO = 'images/logos/logo.png'

DEFAULT_CATEGORY = 'grot'

DIRECT_TEMPLATES = ['index', 'categories', 'archives', 'tags']

SITEMAP = {
    'format': 'xml',
    'exclude': ['tags/', 'author/', 'categories/']
}

YUICOMPRESSOR_EXECUTABLE = 'yuicompressor'

ARTICLE_URL = 'letters/{slug}/'
ARTICLE_SAVE_AS = 'letters/{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
DRAFT_URL = 'drafts/{slug}/'
DRAFT_SAVE_AS = 'drafts/{slug}/index.html'
CATEGORY_URL = 'categories/{slug}/'
CATEGORY_SAVE_AS = 'categories/{slug}/index.html'
AUTHOR_SAVE_AS = ''
TAG_URL = 'tags/{slug}/'
TAG_SAVE_AS = 'tags/{slug}/index.html'

ARCHIVES_SAVE_AS = 'letters/index.html'
ARCHIVES_URL = 'letters/'
# SIDTODO: What is this tag?
AUTHORS_SAVE_AS = ''
CATEGORIES_SAVE_AS = 'categories/index.html'
CATEGORIES_URL = 'categories'
TAGS_SAVE_AS = 'tags/index.html'
TAGS_URL = 'tags/'

STATIC_PATHS = [
    'images',
    'static',
    'fonts'
    ]

EXTRA_PATH_METADATA = {
    'static/robots.txt': {'path': 'robots.txt'},
    'images/logos/favicon.png': {'path': 'favicon.png'},
    }

# Theme extras
MENUITEMS = [
  ('Letters', 'letters/'),
]

SOCIAL = (
  ('GitHub', 'https://github.com/sidcode'),
  ('LinkedIn', 'https://www.linkedin.com/in/sidcode/'),
)

TWITTER_HANDLE = "@readyplayersid"
SITEMETA = "sidcode's scribes/stories"
