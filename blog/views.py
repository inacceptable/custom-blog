from django.shortcuts import render
from django.http  import HttpResponse
from .models import blog_change 
from .models import topic 
from .models import blog_post 
from .models import home_page_section 
from django.http import JsonResponse
from  blog.forms import section_form 
from blog.forms import topic_form, image_form, post_form
import os 
from django.http import JsonResponse



def home(request):
	changes = blog_change.objects.get()
	topic_item = topic.objects.all() 
	page_section = home_page_section.objects.all() 

	total_topics = len(topic_item)
	context = {	
		'changes' : changes, 
		
		'topic_item' : topic_item, 
		'total_topics' : total_topics, 
		'page_section' : page_section, 
	}
	return render(request, 'html/home.html', context)

def get_topic(request): 
	test = request.GET['topic']
	changes = blog_change.objects.get()
	topic_item = topic.objects.all() 
	get_posts = blog_post.objects.filter(topic=test)
	context = { 
		'get_posts' : get_posts,
		'topic_item' : topic_item, 
		'changes' : changes, 
	}
	return render(request, 'html/topic.html', context)

def post(request):
	test = request.GET['post']
	try:
		changes = blog_change.objects.get()
	except: 
		print("Not working!")
	x = blog_post.objects.get(post_id=test)
	post_item = blog_post.objects.all() 
	topic_item = topic.objects.all() 
	get_posts = blog_post.objects.filter(post_id=test)
	context = { 
		'topic' : x,
		'get_posts' : get_posts,
		'topic_item' : topic_item, 
		'changes' : changes, 
	}
	return render(request, 'html/post.html', context) 

def controladmin(request):
	all_topics = topic.objects.all()
	page_range = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
	color_count = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
	changes = blog_change.objects.get()
	page_section = home_page_section.objects.all() 
	all_posts = blog_post.objects.all() 
	form = section_form() 
	form_topic = topic_form()
	form_image = image_form() 
	post_form1 = post_form() 
	context ={
		'page_range' : page_range,
		'color_count' : color_count, 
		'all_topics' : all_topics,
		'changes' : changes, 
		'page_section' : page_section,
		'all_posts' : all_posts,
		'form' : form,
		'form_topic' : form_topic,
		'image_form' : form_image, 
		'post_form' : post_form1,
	}
	return render(request, "html/admin.html", context)

def change_color(request): 
	user_input = str(request.GET.get('color_value_new'))
	url = str(request.GET.get('pass_url'))
	my_filter = {}
	user_input_new = ""
	user_input_new = "#" + user_input 
	my_filter[url] = user_input_new
	blog_change.objects.filter(header_id=1).update(**my_filter)
	message = 'This has been updated!'
	data = {'response': message, 'user_input_new' : user_input_new}
	return JsonResponse(data)

def change_text(request): 
	user_input = str(request.GET.get('new_text_value'))
	url = str(request.GET.get('pass_url'))
	my_filter = {}
	my_filter[url] = user_input
	blog_change.objects.filter(header_id=1).update(**my_filter)
	message = 'This has been updated!'
	data = {'response': message, 'user_input' : user_input}
	return JsonResponse(data)


def update_topic(request): 
	user_input = str(request.GET.get('new_text_value'))
	header_id = str(request.GET.get('header_id'))
	url = str(request.GET.get('item_to_update'))
	my_filter = {}
	my_filter[url] = user_input 
	home_page_section.objects.filter(section_id=header_id).update(**my_filter)
	message = 'This has been updated!'
	data = {'response': message, 'user_input' : user_input}
	return JsonResponse(data)

def update_topic_for_post(request):
	header_id = request.GET.get('header_id')
	user_input = str(request.GET.get('text_value'))
	user_input = int(user_input)
	header_id = int(header_id)
	topic_object = topic.objects.get(header_id = header_id)
	new_blog = blog_post.objects.get(post_id=user_input)
	new_blog.topic = topic_object 
	new_blog.save() 
	message = 'This has been updated!'
	data = {'user_input' : user_input}
	return JsonResponse(data)


def update_topic_select(request): 
	user_input = request.GET.get('new_text_value')
	header_id = str(request.GET.get('header_id'))
	url = request.GET.get('item_to_update')
	home_page_section.objects.filter(section_id=header_id).update(post=user_input)
	message = 'This has been updated!'
	data = {'response': message, 'user_input' : user_input}
	return JsonResponse(data)


def update_topic_text(request): 
	user_input = request.GET.get('new_text_value')
	header_id = request.GET.get('header_id')
	url = str(request.GET.get('item_to_update'))
	my_filter = {}
	my_filter[url] = user_input 
	topic.objects.filter(header_id=header_id).update(**my_filter)
	message = 'This has been updated!'

	data = {'response': message, 'user_input' : user_input}
	return JsonResponse(data)

def update_additional_section_photo(request):
    file = request.FILES.get('file')
    header_id = request.POST.get('header_id')
    my_filter = {}
    my_filter['section_id'] = header_id 
    image_object = home_page_section.objects.get(**my_filter)

    image_object.header_image = request.FILES.get('file')
    image_object.save()
    message = 'Image has been changed'
    url = "http://127.0.0.1:8000" + image_object.header_image.url
    data = {'url' : url}
    return JsonResponse(data)

def update_topic_photo(request):
    file = request.FILES.get('file')
    header_id = request.POST.get('header_id')
    my_filter = {}
    my_filter['header_id'] = header_id 
    image_object = topic.objects.get(**my_filter)

    image_object.topic_image = request.FILES.get('file')
    image_object.save()
    message = 'Image has been changed'
    url = "http://127.0.0.1:8000" + image_object.topic_image.url
    data = {'url' : url}
    return JsonResponse(data)


def add_a_new_section(request):

    title = str(request.POST.get('section_title')) 
    content = str(request.POST.get('section_content'))
    post = str(request.POST.get('post_id'))
    post = int(post)
    postid = blog_post.objects.get(post_id=post)
    new_object = home_page_section(section_title=title, header_image=request.FILES.get('file'), post=postid, section_content=content) 
    new_object.save() 
    message = 'This has been saved'
    data = {'response': message}
    return JsonResponse(data)

def add_a_new_post(request):

    title = str(request.POST.get('post_title')) 
    description = str(request.POST.get('post_description'))
    post_preview_text = str(request.POST.get('post_preview_text'))
    post_t = str(request.POST.get('post_topic'))
    post_t = int(post_t)
    topic_id = topic.objects.get(header_id=post_t)
    new_object = blog_post(topic=topic_id, post_title=title, post_preview_text=post_preview_text, description=description) 
    new_object.save() 
    message = 'This has been saved'
    data = {'response': message}
    return JsonResponse(data)


def add_a_new_topic(request):
    topic_name = str(request.POST.get('topic_name')) 
    topic_description = str(request.POST.get('topic_description'))
    new_object = topic(topic_name=topic_name, topic_image=request.FILES.get('file'), topic_description=topic_description) 
    new_object.save() 
    message = 'This has been saved'
    data = {'response': message}
    return JsonResponse(data)

def delete_section(request): 
	section = str(request.GET.get('header_id'))
	section = int(section)
	section_to_delete = home_page_section.objects.get(section_id=section)
	home_page_section.objects.get(section_id=section).delete()
	message = "This has been deleted" 
	data = {'response' : message}
	return JsonResponse(data) 


def delete_topic(request): 
	section = str(request.GET.get('header_id'))
	section = int(section)
	section_to_delete = topic.objects.get(header_id=section)
	topic.objects.get(header_id=section).delete()
	message = "This has been deleted" 
	data = {'response' : message}
	return JsonResponse(data) 

def delete_post(request): 
	section = str(request.GET.get('header_id'))
	section = int(section)
	blog_post.objects.get(post_id=section).delete()
	message = "This has been deleted" 
	data = {'response' : message}
	return JsonResponse(data) 


def update_post(request): 
	post_id = request.POST.get('post_id')
	post_update = str(request.POST.get('post_update')) 
	item_to_update = str(request.POST.get('item_to_update'))
	my_filter = {}
	my_filter[item_to_update] = post_update  
	blog_post.objects.filter(post_id = post_id).update(**my_filter)
	message = 'This has been updated!'
	data = {}
	return JsonResponse(data)