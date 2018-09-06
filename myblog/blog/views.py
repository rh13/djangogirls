from django.shortcuts import render, redirect
from django.utils import timezone
from .models import blog_post
from .forms import postForm

# Create your views here.

def post_list(request):
	posts = blog_post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts': posts})


def post_details(request, post_id):
	post = blog_post.objects.get(pk=post_id)
	print(post)
	return render(request, 'blog/post_details.html', {'post': post})

def new_post(request):
	if request.method == 'POST':
		form = postForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_details', post.pk)

	else:
		form = postForm()
	return render(request, 'blog/new_post.html', { 'form':form})


def edit_post(request, post_id):
    post = blog_post.objects.get(pk=post_id)
    if request.method == 'POST':
    	form = postForm(request.POST, instance=post)
    	if form.is_valid():
    		form.save()
    		return redirect('post_details', post.pk)
    else:
        form = postForm(instance=post)
    return render(request, 'blog/edit_post.html', { 'form' : form})

