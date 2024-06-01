from django import forms
from django.forms.widgets import NumberInput
from django.core import validators
COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('g', 'Green'),
    ('b', 'Black'),
    ('r', 'Red'),
      ]
Food_CHOICES = [
    ('P', 'Pizza'),
    ('G', 'Burger'),
    ('S', 'Sandwich'),
    ('M', 'Milkshake'),
    ('F', 'Fried chicken'),
]
class MyForm(forms.Form):
    name = forms.CharField(initial='Your name' , validators=[validators.MaxLengthValidator(10, message='Enter a name with at least 10 characters')])
    email = forms.EmailField(label="Please enter your email address",)
    birth_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    date = forms.DateField( widget=forms.DateInput(attrs={'class': 'date-class', 'type': 'date'}))
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    appointment = forms.CharField(widget=forms.DateInput(attrs= {'type' : 'datetime-local'}))
    Multiple_food = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=Food_CHOICES,)
    favorite_color = forms.ChoiceField(choices=COLORS_CHOICES, widget=forms.RadioSelect)
    Decimal_value = forms.DecimalField(required = False)
    password = forms.CharField(widget=forms.PasswordInput)
    file = forms.FileField(required = False)
    agree = forms.BooleanField(initial=False)
    


