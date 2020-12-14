from django import forms


class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    bootcatcher = forms.CharField(required=False, widget=forms.HiddenInput)

    def clean_bootcatcher(self):
        bootcatcher = self.cleaned_data['bootcatcher']
        if len(bootcatcher) > 0:
            raise forms.ValidationError('GOTCHA BOT!')
        return bootcatcher
