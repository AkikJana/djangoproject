from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts
#import requests
# Create your views here.
def index(request):

	posts=Posts.objects.all()[:10]
	context={
	'title':'Latest Posts',
	'posts':posts
	}
	#return HttpResponse('hello from posts')
	return render(request,'posts/index.html',context)

	