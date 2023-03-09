from django import forms
from .models import Question, Category

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = [
            'title',
            'description',
            'category',
        ]

    title=forms.CharField(
        widget=forms.TextInput(attrs={
            'class':'question-form-field',
    }))

    description=forms.CharField(
        widget=forms.Textarea(attrs={
            'class':'question-form-textarea',
    }))

    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        empty_label="(Nenhum)",
        widget=forms.Select(attrs={
            'class':'question-choicefield'
        })
    )


