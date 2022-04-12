from django import forms

from Boca.paginas.views import option
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
        
class optionForm(forms.ModelForm):

    #metaclase
    class Meta:
        model = option

        #especificar los campos
        fields = [
            'UserName',
            'UserFullName',
            'UserDescription', 
            'OldPassword',
            'NewPassword',
            'RetypeNewPassword',
        ]