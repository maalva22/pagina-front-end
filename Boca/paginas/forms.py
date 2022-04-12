from django import forms
from .models import contest
 

class contestForm(forms.ModelForm):

    #metaclase
    class Meta:
        model = contest

        #especificar los campos
        fields = [
            'Numero',
            'Name',
            'startDate', 
            'Duration',
            'StopAnswering',
            'StopScoreboard',
            'Penalty',
            'MaxFileSize',
            'URL',
            'ContestM',
            'ContestL',
        ]