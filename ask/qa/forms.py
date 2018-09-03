from django import forms
from qa.models import Question, Answer

class AskForm(forms.Form):
    title = forms.CharField(widget=forms.Textarea)
    text = forms.CharField(widget=forms.Textarea)

    def clean_title(self):
        title = self.cleaned_data['title']
        if not title:
            raise forms.ValidationError(
                u'Поле не может быть пустым', code='empty value'
                )
        return title.upper()

    def clean_text(self):
        text = self.cleaned_data['text']
        if not text:
            raise forms.ValidationError(
                u'Поле не может быть пустым', code='empty value'
                )
        return text.lower()

    def save(self):
        question = Question(**self.cleaned_data)
        question.save()
        return question

    def clean(self):
        return self.cleaned_data
    #     # print()
    #     raise forms.ValidationError(
    #     u'Сообщение похоже на спам!', code='spam'
    #     )

class AnswerForm(forms.Form):
    text = forms.CharField()
    # text = forms.CharField(widget=forms.Textarea)
    question = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(AnswerForm, self).__init__(*args, **kwargs)

    def clean_text(self):
        text = self.cleaned_data['text']
        if not text:
            raise forms.ValidationError(
                u'Поле не может быть пустым', code='empty value'
                )
        return text

    def clean_question(self):
        question = self.cleaned_data['question']
        if not question:
            raise forms.ValidationError(
                u'Поле не может быть пустым', code='empty value'
                )
        return question

    def clean(self):
        return self.cleaned_data

    def save(self):
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer
