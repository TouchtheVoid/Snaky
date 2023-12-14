from django import forms
from .models import BlogPost, Comment, Image


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'text']
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [ 'text']
class ImageForm(forms.ModelForm):
    class Meta:
        model= Image
        fields =['image']