from django.contrib import admin
from .models import Post

admin.site.site_header = 'Wanderer Admin'
admin.site.site_title = 'Wanderer Admin Area'
admin.site.index_title = 'Welcome to the Wanderer Admin Area'


admin.site.register(Post)
