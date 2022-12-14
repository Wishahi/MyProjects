from django import forms
from datetime import date
from.models import (
Director,
Film,
Poster,
Comment,
Review
)


class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = '__all__'
        widgets = {
            'released_date': forms.DateInput(attrs= {'type': 'date'}) 
            

        }

class DirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = '__all__'

class PosterForm(forms.ModelForm):
    class Meta:
        model = Poster
        fields = '__all__'
        

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'

class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ["stars"]

                