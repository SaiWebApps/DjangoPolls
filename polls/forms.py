from django import forms
from django.forms import ModelForm
from polls.models import Poll, Choice

def required_msg(val):
    return {'required' : 'Please enter a ' + val + '.'}

class PollForm(ModelForm):
    question = forms.CharField(max_length=200, error_messages=required_msg("question"))
    class Meta:
        model = Poll
        fields = ['question']
        
class ChoiceForm(ModelForm):
    choice_text = forms.CharField(max_length=200, error_messages=required_msg("choice"))
    class Meta:
        model = Choice
        fields = ['choice_text']