from django import forms
from django.core import validators


# def check_for_z(value):
#     if value[0].lower() != 'z':
#         raise forms.ValidationError('NAME NEEDS TO START WITH Z')


class FormName(forms.Form):
    # name = forms.CharField(validators=[check_for_z])
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label="enter your email again")
    text = forms.CharField(widget=forms.Textarea)
    bootcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[
                                  validators.MaxLengthValidator(0)])

    # def clean_bootcatcher(self):
    #     bootcatcher = self.cleaned_data['bootcatcher']
    #     if len(bootcatcher) > 0:
    #         raise forms.ValidationError('GOTCHA BOT!')
    #     return bootcatcher

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vemail = all_clean_data['verify_email']

        if email != vemail:
            raise forms.ValidationError('MAKE SURE EMAILS MATCH')
