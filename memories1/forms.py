from django import forms
from .models import Post



#________________________________________________________________________________POSTFORM
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


#________________________________________________________________________________POSTDELETEFORM
class PostDeleteForm(forms.Form):
    confirm = forms.BooleanField(
        required=True,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
    )
