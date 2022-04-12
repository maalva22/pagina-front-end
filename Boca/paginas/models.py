from email.policy import default
from django.db import models
from django.forms import IntegerField

# Create your models here.

class contest(models.Model):
    
    Numero=models.IntegerField()
    Name = models.CharField(max_length=200)
    startDate = models.DateField()
    Duration=models.IntegerField()
    StopAnswering=models.IntegerField()
    StopScoreboard=models.IntegerField()
    Penalty=models.IntegerField()
    MaxFileSize=models.IntegerField()
    URL= models.CharField(max_length=200, default="Link")
    ContestM=models.IntegerField()
    ContestL=models.IntegerField()

    def get_Numero(self):
        return self.Numero

    def get_Name(self):
        return self.Name
        
    def get_StartDate(self):
        return self.startDate
        
    def get_Duration(self):
        return self.Duration
        
    def get_StopAnswering(self):
        return self.StopAnswering
        
    def get_StopScoreBoard(self):
        return self.StopScoreboard
        
    def get_Penalty(self):
        return self.Penalty

    def get_MaxFileSize(self):
        return self.MaxFileSize

    def get_URL(self):
        return self.URL

    def get_ContestM(self):
        return self.ContestM

    def get_ContestL(self):
        return self.ContestL

    def __str__(self):
        texto= "{0} ({1})"
        return texto.format(self.Name, self.Numero)