from django import forms
from .models import Topic

class NewTopicForm(forms.ModelForm):
    message = forms.CharField(
    	widget=forms.Textarea(
    		attrs={'rows':5,'placeholder':'主題內容'}),
    	max_length=4000,
    	help_text='文字長度不可超過4000')

    class Meta:
        model = Topic
        fields = ['subject', 'message']