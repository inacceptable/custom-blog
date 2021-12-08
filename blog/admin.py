from django.contrib import admin
from .models import blog_change, topic, blog_post, home_page_section 

admin.site.register(blog_change)
admin.site.register(topic)
admin.site.register(blog_post)
admin.site.register(home_page_section)