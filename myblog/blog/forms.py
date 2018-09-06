from django import forms
from .models import blog_post

class postForm(forms.ModelForm):
	class Meta():
		model = blog_post
		fields = ('title', 'description',)