from django import forms
from .models import Show
import datetime
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout, Row, Column, Submit

class ShowForm(forms.ModelForm):
    # To add bootstrap classes for all inputs
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
        # self.helper = FormHelper()
        # self.helper.layout = Layout(
        #     'title',
        #     Row(
        #         Column('network', css_class='form-group col-md-2'),
        #         Column('release_date', css_class='form-group col-md-2'),
        #         css_class='form-row'
        #     ),
        #     'description',
        # )

    release_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    description = forms.CharField(label='Description', widget=forms.Textarea(attrs={'rows': 5}), required=False)
    
    class Meta:
        model = Show
        # exclude = ['created_at', 'updated_at']
        fields = ['title', 'network', 'release_date', 'description']

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        network = cleaned_data.get('network')
        release_date = cleaned_data.get('release_date')
        description = cleaned_data.get('description')

        # Get the instance being updated if available
        instance = getattr(self, 'instance', None)

        if len(title) < 3:
            self.add_error('title', "Show title should be at least 3 characters")
          # Check if there's an existing show with the same title but different ID
        if Show.objects.filter(title=title).exclude(pk=instance.pk).exists():
            self.add_error('title', "This show title already exists! It should be unique")

        if not network.isalpha() or len(network) < 4:
            self.add_error('network', "Network name cannot contain numbers or special characters and should be at least 4 characters long")

        if  release_date > datetime.date.today():
            self.add_error('release_date', "Release date cannot be in the future")

        if description and len(description) < 10:
            self.add_error('description', "Description should be at least 10 characters or empty")