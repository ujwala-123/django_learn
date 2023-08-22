from django import forms
from .models import User
from .models import Author
from .models import Publisher
from .models import Books

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['firstname', 'lastname', 'address', 'zipcode', 'telephone', 'recommendedby', 'joindate', 'popularity_score','followers']

class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ['firstname', 'lastname', 'recommendedby', 'joindate', 'popularity_score']
        
class BooksForm(forms.ModelForm):
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    class Meta:
        model = Books
        fields = ['title', 'genre', 'price', 'published_date', 'author', 'publisher']
        
