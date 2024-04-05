from django import forms
from .models import Show
import datetime

class ShowForm(forms.ModelForm):
    release_date = forms.DateField(widget=forms.SelectDateWidget)
    class Meta:
        model = Show
        # exclude = ['created_at', 'updated_at']
        fields = ['title', 'network', 'release_date', 'description']

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 3:
            raise forms.ValidationError("Show title should be at least 3 characters")
        if Show.objects.filter(title=title).exists():
            raise forms.ValidationError("This show title already exists! It should be unique")
        return title

    def clean_network(self):
        network = self.cleaned_data.get('network')
        if not network.isalpha() or len(network) < 4:
            raise forms.ValidationError("Network name cannot contain numbers or special characters and should be at least 4 characters long")
        return network

    def clean_release_date(self):
        release_date = self.cleaned_data.get('release_date')
        if release_date.month == datetime.datetime.now().month and release_date.year == datetime.datetime.now().year:
            raise forms.ValidationError("Release date cannot be in the current month and year")
        return release_date

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if len(description) < 10:
            raise forms.ValidationError("Description should be at least 10 characters or empty")
        return description

    # def clean(self):
    #     super().clean()
    #     cleaned_data = self.cleaned_data
    #     title = cleaned_data.get('title')
