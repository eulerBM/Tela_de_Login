from django.db import models

class banco_de_login(models.Model):
    nome = models.CharField(max_length=30)
    username = models.CharField(max_length=80)
    senha = models.CharField(max_length=20)
    email = models.EmailField()
    

