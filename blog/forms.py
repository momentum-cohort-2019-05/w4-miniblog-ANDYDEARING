from django import forms

class MakeComment(forms.Form):
    # renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")
    new_comment = forms.CharField(help_text="Enter your comment here.", required=True)