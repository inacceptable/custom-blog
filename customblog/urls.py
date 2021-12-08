"""customblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from blog import views
from django.conf import settings 
from django.conf.urls.static import static    
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'), 
    path('topic', views.get_topic, name='topic'),
    path('post', views.post, name='post'),  
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('controladmin', views.controladmin, name='controladmin'), 
    path('change_color', views.change_color, name='change_color'), 
    path('change_text', views.change_text, name='change_text'), 
    path('update_topic', views.update_topic, name='update_topic'), 
    path('update_topic_select', views.update_topic_select, name='update_topic_select'), 
    path('update_topic_text', views.update_topic_text, name='update_topic_text'), 
    path('update_additional_section_photo', views.update_additional_section_photo, name='update_additional_section_photo'),
    path('update_topic_photo', views.update_topic_photo, name='update_topic_photo'),
    path('add_a_new_section', views.add_a_new_section, name='add_a_new_section'), 
    path('add_a_new_topic', views.add_a_new_topic, name='add_a_new_topic'), 
    path('add_a_new_post', views.add_a_new_post, name='add_a_new_post'), 
    path('delete_section', views.delete_section, name='delete_section'), 
    path('delete_topic', views.delete_topic, name='delete_topic'), 
    path('update_post', views.update_post, name='update_post'), 
    path('update_topic_for_post', views.update_topic_for_post, name='update_topic_for_post'),
    path('delete_post', views.delete_post, name='delete_post')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

