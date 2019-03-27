from django import forms

from .models import Professor, Comment

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author','rating', 'text',)
