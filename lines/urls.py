from django.conf.urls import url, include

import lines.views


lines_patterns = [
url('^search/$', lines.views.search, name='search'),

url('^hot/$', lines.views.line_content, {'line_name': 'hot'}, name='hot'),
url('^cold/$', lines.views.line_content, {'line_name': 'cold'}, name='cold'),
url('^pizza/$', lines.views.line_content, {'line_name': 'pizza'}, name='pizza'),
url('^pasta/$', lines.views.line_content, {'line_name': 'pasta'}, name='pasta'),
url('^dessert/$', lines.views.line_content, {'line_name': 'dessert'}, name='dessert'),
url('^bar/$', lines.views.line_content, {'line_name': 'bar'}, name='bar'),

url(r'^(?P<line_name>[\w\-]+)/(?P<recipe_slug>[\w\-]+)/details/$', lines.views.recipe_details, name='recipe_details'),
url(r'^(?P<line_name>[\w\-]+)/(?P<recipe_slug>[\w\-]+)/ingridients/$', lines.views.recipe_ingridients, name='recipe_ingridients'),
url(r'^(?P<line_name>[\w\-]+)/(?P<recipe_slug>[\w\-]+)/technology/$', lines.views.recipe_technology, name='recipe_technology'),
]

urlpatterns = [url(r'^$', lines.views.toSearch, name='redirect_to_lines_search'),
               url(r'^lines/', include(lines_patterns))
               ]