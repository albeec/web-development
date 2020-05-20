from django import forms
from .models import BlogPost

class BlogPostForm(forms.Form):
    name = forms.CharField()
    slug = forms.SlugField()
    content = forms.CharField(widget=forms.Textarea)


class BlogPostModelForm(forms.ModelForm):
	class Meta:
		model = BlogPost
		fields = ['title', 'slug', 'content', 'publish_date']