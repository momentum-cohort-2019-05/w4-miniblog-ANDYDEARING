from django import forms

class MakeComment(forms.Form):
    new_comment = forms.CharField(help_text="Enter your comment here.", required=True)