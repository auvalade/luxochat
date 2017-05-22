from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
 
text_only_validator = RegexValidator(r'^[a-zA-Z ]*$', "Ensure this value only contains letters and spaces.")


class AddMessageForm(forms.Form):
    content = forms.CharField(max_length=256, validators=[text_only_validator], label='Message')
    name = forms.CharField(max_length=20, validators=[text_only_validator], label='Name')

