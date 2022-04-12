from django import forms
from .models import contest
 

class contestForm(forms.ModelForm):

    #metaclase
    class Meta:
        model = contest

        #especificar los campos
        fields = [
            'Number',
            'Name', 
            'start_Date', 
            'Duration',
            'Stop_Answering',
            'Stop_Scoreboard',
            'Penalty',
            'Max_file_size_allowed_for_teams',
            'Contest_mainsite_URL',
            'Contest_Main_site_number',
            'Contest_local_site_numer',

            
        ]