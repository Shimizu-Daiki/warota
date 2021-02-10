from django import forms
from .models import Answer

class AnswerForm(forms.ModelForm):

    class Meta:
        model = Answer
        fields = ('name','text')
        widgets = {
                    'name': forms.TextInput(attrs={'placeholder':'記入例：山田　太郎'}),
                    'text': forms.TextInput(attrs={'rows':1}),
                  }