from django.db import models

# Create your models here.

class Pessoa(models.Model):
    GENEROS = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outros'),
    )

    nome = models.CharField(
        max_length = 255,
        verbose_name = 'Nome'
    )

    sobrenome = models.CharField(
        max_length = 255,
        verbose_name = 'Sobrenome'
    )

    genero = models.CharField(
        max_length = 255,
        verbose_name = 'Gênero',
        choices = GENEROS
    )

    email = models.EmailField(
        max_length = 255,
        verbose_name = 'E-mail'
    )

    data_de_criacao = models.DateTimeField(
        auto_now_add = True
    )

    ativo = models.BooleanField(
        default = True
    )


    def __str__(self):
        return str(self.nome + ' ' + self.sobrenome)


