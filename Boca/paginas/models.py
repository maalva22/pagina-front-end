from django.db import models

# Create your models here.

class contest(models.Model):
    Name = models.CharField(max_length=200)
    startDate = models.DateField()

    def get_indiceA(self):
        return self.Aindice
    def get_nombreA(self):
        return self.nombreA
        
    def __str__(self):
        texto= "{0} ({1})"
        return texto.format(self.Aindice +' '+self.nombreA, self.id)