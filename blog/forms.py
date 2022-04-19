from django import forms
from .models import Comment
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from ckeditor.fields import RichTextField

# Apply summernote to specific fields.
class SomeForm(forms.Form):
    message = RichTextField ()
    foo = forms.CharField(widget=SummernoteWidget())  # instead of forms.Textarea

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name','email','message','website',]




