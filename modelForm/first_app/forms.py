from django import forms 

from .models import Mymodel
class MymodelForm(forms.ModelForm):
    class Meta:
        model = Mymodel
        fields='__all__'
        widgets={
            'time_field': forms.TimeInput(attrs={'type': 'time'}),
            'date_field': forms.DateInput(attrs={'type': 'date'}),
            'date_time_field': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }