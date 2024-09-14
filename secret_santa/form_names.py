from django import forms


class ParticipantForm(forms.Form):
    name = forms.CharField(max_length=50)

    def clean_name(self):
        name = self.cleaned_data.get("name")
        return name
