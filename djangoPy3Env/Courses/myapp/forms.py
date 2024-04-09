from django import forms
from .models import Comment
# Form to add new course and description
class CourseDescriptionForm(forms.Form):
    name = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea(attrs={'rows': 5}))

# Validation Function
    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        description = cleaned_data.get('description')

        if len(name) < 5:
            self.add_error('name', "Course name should be at least 5 characters!")

        if len(description) < 15:
            self.add_error('description', "Description should be at least 15 characters!")
        return cleaned_data
    
# Form to add new comment for specific course
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content'] 