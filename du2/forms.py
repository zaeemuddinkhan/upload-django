from django import forms
from . models import Comment

class Commentform(forms.ModelForm):
    class Meta:
        model= Comment
        exclude=["posts"]
        labels={
            "user_name":"Your name",
            "user_email": "Your email",
            "text":"Your comment"
        }
