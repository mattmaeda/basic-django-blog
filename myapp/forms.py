from django.forms import ModelForm, Textarea, TextInput, DateInput
from django.utils.translation import ugettext_lazy as _
from myapp.models import Post, Category


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'author', 'published_date']
        widgets = {
            'title': TextInput(attrs={'size': '80'}),
            'text': Textarea(attrs={'cols': 80, 'rows': 20}),
            'published_date': DateInput(attrs={'class':'datepicker'}),
        }
        labels = {
            'author': _('Your Name'),
            'title': _('Post Title'),
            'text': _('Post Text'),
        }
        error_messages = {
            'title': {
                'max_length': _("This post's title is too long."),
            },
        }



class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description', 'posts']
        widgets = {
            'description': Textarea(attrs={'cols': 80, 'rows': 20}),
        }
        labels = {
            'name': _('Category Name'),
            'desscription': _('Category Description'),
        }
        error_messages = {
            'name': {
                'max_length': _("This category's name is too long."),
            },
        }
