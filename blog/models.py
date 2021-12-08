from django.db import models
from colorfield.fields import ColorField
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class topic(models.Model):
	header_id = models.AutoField(primary_key=True) 
	topic_name = models.CharField(max_length = 100)
	topic_image = models.ImageField(upload_to='images/', null=True)
	topic_description = models.CharField(max_length=200)
	def __str__(self):
		return self.topic_name
 

class blog_change(models.Model):
	header_id = models.AutoField(primary_key=True) 
	header_title = models.CharField(max_length =50)
	header_image = models.ImageField(upload_to='images/', null=True)
	header_slogan = models.CharField(max_length=100) 
	header_border_background_color = ColorField(default='#FF0000')
	header_background_color = ColorField(default='#FF0000')
	header_slogan_background_color = ColorField(default='#FF0000') 
	header_slogan_top_background_color = ColorField(default='#FF0000') 
	header_slogan_font_color = ColorField(default='#FF0000')
	header_title_font_color = ColorField(default='#FF0000') 
	navigation_button_text_color = ColorField(default='#FF0000')
	navigation_bar_background_color = ColorField(default='#FF0000')
	navigation_button_background_color = ColorField(default='#FF0000')
	navigation_bar_sub_buttons_background_color = ColorField(default='#FF0000')
	navigation_bar_sub_button_font_color = ColorField(default='#FF0000')
	navigation_drop_down_background_color = ColorField(default='#FF0000')
	section_button_background_color = ColorField(default='#FF0000') 
	section_button_font_color = ColorField(default='#FF0000') 
	section_background_color = ColorField(default='#FF0000') 
	section_header_font_color = ColorField(default='#FF0000')
	section_text_font_color = ColorField(default='#FF0000')
	section_border_color = ColorField(default='#FF0000')
	def __str__(self): 
		return self.header_title

class blog_post(models.Model):
	post_id = models.AutoField(primary_key=True)
	topic = models.ForeignKey(topic, on_delete=models.CASCADE, null='True', blank=True)
	post_title = models.TextField() 
	post_preview_text = models.CharField(max_length=300)
	description = models.TextField() 
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)	
	def __str__(self):
		return self.post_title


class home_page_section(models.Model): 
	section_id = models.AutoField(primary_key=True)
	section_title = models.CharField(max_length=300) 
	header_image = models.ImageField(upload_to='images/', null=True, blank=True)
	post = models.ForeignKey(blog_post, on_delete=models.DO_NOTHING)
	section_content = models.TextField() 
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	def __str__(self):
		return self.section_title


