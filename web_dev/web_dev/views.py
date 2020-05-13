from django.http import HttpResponse
from django.shortcuts import render 

from .forms import ContactForm

def home_page(request):
	return render(request, "home_page.html")


def about_page(request):
	return render(request, "about_page.html")


def contact_page(request):
	print(request.POST)
	form = ContactForm(request.POST or None)
	if form.is_valid():
		print(form.cleaned_data)

	return render(request, "contact_page.html", {"form": form})
	
