from django.db import models
from colorfield.fields import ColorField

class topic(models.Model):
	header_id = models.AutoField(primary_key=True) 
	topic_name = models.CharField(max_length = 100)
	topic_image = models.ImageField(upload_to='images/')
	topic_description = models.CharField(max_length=200)
	def __str__(self):
		return self.topic_name
 

class blog_change(models.Model):
	header_id = models.AutoField(primary_key=True) 
	header_title = models.CharField(max_length =50)
	header_image = models.ImageField(upload_to='images/')
	header_slogan = models.CharField(max_length=100) 
	header_border_background_color = ColorField(default='#B9FFE9')
	header_background_color = ColorField(default='#1B2344')
	header_slogan_background_color = ColorField(default='#979797') 
	header_slogan_top_background_color = ColorField(default='#9E9E9E') 
	header_slogan_font_color = ColorField(default='#88FFC2')
	header_title_font_color = ColorField(default='#FFE623') 
	navigation_button_text_color = ColorField(default='#2EFFFF')
	navigation_bar_background_color = ColorField(default='#B9FFCE')
	navigation_button_background_color = ColorField(default='#868AFF')
	navigation_bar_sub_buttons_background_color = ColorField(default='#46CDFF')
	navigation_bar_sub_button_font_color = ColorField(default='#5E73BB')
	navigation_drop_down_background_color = ColorField(default='#1B2344')
	section_button_background_color = ColorField(default='#4976FD') 
	section_button_font_color = ColorField(default='#FBFFAE') 
	section_background_color = ColorField(default='#A5AEE9') 
	section_header_font_color = ColorField(default='#FFFFFF')
	section_text_font_color = ColorField(default='#FF0000')
	section_border_color = ColorField(default='#979797')
	def __str__(self): 
		return self.header_title

class blog_post(models.Model):
	post_id = models.AutoField(primary_key=True)
	topic = models.ForeignKey(topic, on_delete=models.CASCADE, )
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
	header_image = models.ImageField(upload_to='images/')
	post = models.ForeignKey(blog_post, on_delete=models.DO_NOTHING)
	section_content = models.TextField() 
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	def __str__(self):
		return self.section_title


