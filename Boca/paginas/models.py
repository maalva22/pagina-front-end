from email.policy import default
from django.db import models
from django.forms import IntegerField
from django.contrib.auth.backends import BaseBackend

# Create your models here.

class contest(models.Model):
    
    Number=models.IntegerField()
    Name = models.CharField(max_length=200)
    start_Date = models.DateField()
    Duration=models.IntegerField()
    Stop_Answering=models.IntegerField()
    Stop_Scoreboard=models.IntegerField()
    Penalty=models.IntegerField()
    Max_file_size_allowed_for_teams=models.IntegerField()
    Contest_mainsite_URL= models.CharField(max_length=200)
    Contest_Main_site_number=models.IntegerField()
    Contest_local_site_numer=models.IntegerField()

    def get_Numero(self):
        return self.Number

    def get_Name(self):
        return self.Name
        
    def get_StartDate(self):
        return self.start_Date
        
    def get_Duration(self):
        return self.Duration
        
    def get_StopAnswering(self):
        return self.Stop_Answering
        
    def get_StopScoreBoard(self):
        return self.Stop_Scoreboard
        
    def get_Penalty(self):
        return self.Penalty

    def get_MaxFileSize(self):
        return self.Max_file_size_allowed_for_teams

    def get_URL(self):
        return self.Contest_mainsite_URL

    def get_ContestM(self):
        return self.Contest_Main_site_number

    def get_ContestL(self):
        return self.Contest_local_site_numer

    def __str__(self):
        texto= "{0} ({1})"
        return texto.format(self.Name, self.Number)

class option(models.Model):
    
        Username=models.CharField(max_length=200)
        User_Full_Name = models.CharField(max_length=200)
        User_Description = models.CharField(max_length=500)
        Old_Password=models.CharField(max_length=200)
        New_Password=models.CharField(max_length=200)
        Retype_New_Password=models.CharField(max_length=200)
    

        def get_UserName(self):
            return self.Username

        def get_UserFullName(self):
            return self.User_Full_Name
        
        def get_UserDescription(self):
            return self.User_Description
        
        def get_OldPassword(self):
            return self.Old_Password
        
        def get_NewPassword(self):
            return self.New_Password
        
        def get_RetypeNewPassword(self):
            return self.Retype_New_Password
        
    

        def _str_(self):
            texto= "{0} ({1})"
            return texto.format(self.Username, self.User_Full_Name)