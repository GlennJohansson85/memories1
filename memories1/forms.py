from django.core.exceptions import ValidationError
from .models import Post, Comment
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image', 'categories']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['categories'].widget.attrs.update({'class': 'form-control'})
        if user:
            self.user = user

    def save(self, commit=True):
        post = super(PostForm, self).save(commit=False)
        if hasattr(self, 'user'):
            post.user = self.user

        if commit:
            post.save()

        return post


class PostDeleteForm(forms.Form):
    confirm = forms.BooleanField(
        required=True,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
    )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

    def save(self, user, post, commit=True):
        comment = super().save(commit=False)
        comment.user = user
        comment.post = post

        if commit:
            comment.save()