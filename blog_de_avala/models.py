from django.db import models

class Sobre (models.Model):
    escola = models.CharField(max_length=50)
    curso = models.CharField(max_length=20)
    ano = models.IntegerField()
    turno = models.CharField(max_length=50)
    esportes = models.CharField(max_length=200)
    projetos = models.TextField()


    def _str_(self):
        return self.escola
    
class Pessoa (models.Model):
    nome = models.CharField(max_length=50)
    idade = models.IntegerField()
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=11)
    email = models.EmailField(max_length=100)
    endereco = models.CharField(max_length=100)
    estado = models.CharField(max_length=40)
    cidade = models.CharField(max_length=50)
    genero = models.CharField(max_length=15)
    estado_civil = models.CharField(max_length=20)
    foto = models.ImageField(upload_to='fotos/', null=True, blank=True)
    sobre = models.ForeignKey(Sobre, on_delete=models.CASCADE)
    
    def _str_(self):
        return self.nome
# Create your models here.
