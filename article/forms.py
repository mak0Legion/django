from django import forms
from models import Article, Comment
#from django.contrib.auth.models import User
#from django.contrib.auth.forms import UserCreationForm

class ArticleForm(forms.ModelForm):
	
	class Meta:
		model = Article
		fields = ('title', 'body', 'pub_date', 'thumbnail')

class CommentForm(forms.ModelForm):
	
	class Meta:
		model = Comment
		fields = ('name', 'body')

'''class MyRegistrationForm(UserCreationForm):
	email = forms.EmailField(required=True)
	
	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2') 
		
	def save(self, commit=True):
		user = super(UserCreationForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		
		if commit:
			user.save()
			
		return user'''