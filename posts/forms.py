from django import forms
from .models import Post, Category, Comment

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'category']

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название поста'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание поста',
                'rows': 4
            }),
            'category': forms.Select(attrs={
                'class': 'form-select'
            })
        }




class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Write a comment...'})
        }
