from django import forms
from .models import Post, Comment , Post1 ,Comment1


class PostForm(forms.ModelForm):
    body = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows': '4',
            'placeholder': "Say Something..."
        }))

    image = forms.ImageField(required=False)
    videofile = forms.FileField(required=False)

    class Meta:
        model = Post
        fields = ['body','image','videofile']


class CommentForm(forms.ModelForm):
    comment = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows': '3',
            'placeholder': 'Say Something...'
        })
    )

    class Meta:
        model = Comment
        fields = ['comment']

class PostForm1(forms.ModelForm):
    body = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows': '4',
            'placeholder': "Say Something..."
        }))

    image = forms.ImageField(required=False)
    videofile = forms.FileField(required=False)

    class Meta:
        model = Post1
        fields = ['body','image','videofile']


class CommentForm1(forms.ModelForm):
    comment = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows': '3',
            'placeholder': 'Say Something...'
        })
    )

    class Meta:
        model = Comment1
        fields = ['comment']