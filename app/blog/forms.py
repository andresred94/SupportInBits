from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'tags', 'content']
        widgets = {
            'content': forms.Textarea(attrs={'id': 'editor'}),
        }
