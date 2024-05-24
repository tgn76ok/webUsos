from django.db import models

class Urso(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    historia = models.TextField()
    foto = models.ImageField(upload_to='fotos_ursos/')

    def __str__(self):
        return self.nome
    
class Doacao(models.Model):
    username = models.CharField(max_length=150)
    valor = models.FloatField()

    def __str__(self):
<<<<<<< HEAD
        return f"{self.username} - {self.valor}"
=======
        return f"{self.username} - {self.valor}"
    
    
>>>>>>> 3b6a98d641eb06fce2ff737a6d93776dd5666ab7
