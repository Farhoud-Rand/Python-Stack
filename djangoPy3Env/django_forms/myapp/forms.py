from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:              # Inner class defines metadata options for the form
        model = Product      # Specifies which model the form is based on
        fields = '__all__'   # Indicates that all fields from the Product model should be included in the form
    #     widgets = {
    #         'name': forms.TextInput(attrs={'class': 'form-control'}),
    #         'price': forms.NumberInput(attrs={'class': 'form-control'}),
    #         'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
    #     }
        
    # Form use bootstrap
    # CHOICES = (('electronics', 'Electronics'),('clothing', 'Clothing'),('books', 'Books'),('home_and_kitchen', 'Home & Kitchen'))
    # category = forms.ChoiceField(choices=CHOICES, widget= forms.Select(attrs={'class': 'form-control'}) )
        
    # description = forms.CharField(required=False, widget= forms.Textarea(attrs={'class': 'form-control'}))  # Make description field not required

    # Form use crispy form
    CHOICES = (('electronics', 'Electronics'),('clothing', 'Clothing'),('books', 'Books'),('home_and_kitchen', 'Home & Kitchen'))
    category = forms.ChoiceField(choices=CHOICES )
        
    description = forms.CharField(required=False)  # Make description field not required

    # Validation Function
    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        description = cleaned_data.get('description')
        price = cleaned_data.get('price')
        quantity = cleaned_data.get('quantity')

        if len(name) < 4:
            self.add_error('name', "Form 2 --> Product name should be at least 4 characters")

        if description and len(description) < 10:
            self.add_error('description', "Form 2 --> Description should be at least 10 characters or empty")

        if price < 0:
            self.add_error('price', "Form 2 --> Price should be a positive number")

        if quantity < 0:
            self.add_error('quantity', "Form 2 --> Quantity should be a positive number")

        return cleaned_data