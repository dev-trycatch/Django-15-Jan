from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        # fields = ['name','age','email']
        fields = "__all__"
        widgets = {
            'name':forms.TextInput(attrs={
                'class':'fname',
                'placeholder':'Enter your name...',
            }),
            'age':forms.TextInput(attrs={
                'class':'age1',
                'placeholder':'Enter your age...'
            })
        }

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age<=18:
            raise forms.ValidationError('age must be greater than 18')
        return age
    
    