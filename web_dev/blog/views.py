from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.
from .models import BlogPost
from .forms import BlogPostModelForm




def blog_post_detail(request, slug):
	obj = get_object_or_404(BlogPost, slug=slug)
	form = BlogPostModelForm(request.POST or None, instance=obj)
	template_name = 'blog_post_detail.html'
	context = {
		"form": form,
		"isShow": "hidden",
		"object": obj
	}
	return render(request, template_name, context)


def blog_post_list(request):
	#obj = get_object_or_404(BlogPost, slug=slug)
	qs = BlogPost.objects.all().published()
	if request.user.is_authenticated:
		my_qs = BlogPost.objects.filter(user=request.user)
		qs = ( qs | my_qs ).distinct()
	template_name = 'blog_post_list.html'
	context = {"objects": qs}
	return render(request, template_name, context)
	

@login_required(login_url="/admin")
def blog_post_create(request):
	form = BlogPostModelForm(request.POST or None)
	if form.is_valid():
		obj = form.save(commit=False)
		obj.user = request.user
		obj.save()
		form = BlogPostModelForm()
	template_name = 'blog_post_create.html'
	context = {
		"form": form,
		"isShow": "shown"
	}
	return render(request, template_name, context)


def blog_post_update(request, slug):
	print("update")
	print(request.POST)
	obj = get_object_or_404(BlogPost, slug=slug)
	form = BlogPostModelForm(request.POST or None, instance=obj)
	if form.is_valid():
		form.save()
	template_name = 'blog_post_update.html' 
	context = {
		"form": form,
		"isShow": "hidden"
	}
	return render(request, template_name, {"form": form})


def blog_post_delete(request, slug):
	obj = get_object_or_404(BlogPost, slug=slug)
	if request.method == "POST":
		obj.delete()
		return redirect("/blog")
	template_name = 'blog_post_delete.html'
	context = {"object": obj}
	return render(request, template_name, context)
