from django import forms
from .models import Problem

class ProblemForm(forms.ModelForm):

    class Meta:
        model = Problem
        fields = ('name','text')
        widgets = {
                    'name': forms.TextInput(attrs={'placeholder':'記入例：山田　太郎'}),
                    'text': forms.Textarea(attrs={'rows':2}),
                  }
