from django import forms
from blog.models import home_page_section 
from .models import topic, blog_post

from ckeditor.widgets import CKEditorWidget
class section_form(forms.Form):
	section_title = forms.CharField(label = 'Section title ', max_length=50,)
	header_image  = forms.ImageField()
	section_content = forms.CharField(label = 'Section content ', max_length=1000,)

class topic_form(forms.Form): 
	topic_name = forms.CharField(label = 'Topic name ', max_length=50,)
	topic_image  = forms.ImageField()
	topic_description = forms.CharField(label = 'Topic description ', max_length=1000,)

class image_form(forms.ModelForm): 
	class Meta:
		model = home_page_section 
		fields = ("header_image",)


class post_form(forms.Form): 
	post_title = forms.CharField(label = 'Post title ', max_length=50,)
	post_preview_text  = forms.CharField(label = 'Post preview text ', max_length=1000,)
	post_content = forms.CharField(label = 'Post content  ',widget=forms.Textarea )
	post_topic = forms.ModelChoiceField(label = 'Change the topic this post is linked to ', queryset=topic.objects.all())
	
