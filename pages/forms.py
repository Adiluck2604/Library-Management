from django import forms
from .models import Enquiry


class EnquiryForm(forms.Form):
    activity_choices = (
        ("LN", "lend"),
        ("BR", "borrow"),
    )
    full_name = forms.CharField(max_length=64)
    phone_number = forms.CharField(max_length=10)
    activity = forms.ChoiceField(
        choices=activity_choices, label="I wish to", widget=forms.RadioSelect
    )
    college = forms.CharField(max_length=128)
    department = forms.CharField(max_length=64)
    semester = forms.IntegerField(min_value=1, max_value=8)
    subject = forms.CharField(max_length=128)
    book_name = forms.CharField(max_length=128)


class EnquiryModelForm(forms.ModelForm):

    class Meta:
        model = Enquiry
        fields = "__all__"
