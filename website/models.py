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


class Ideia(models.Model):

    CATEGORIAS = (
        ('TERRA_PLANA', 'Terra Plana'),
        ('CONTRA_GROGER', 'Ideias para Coach Groger'),
        ('CONTRA_JOAO', 'Ideias de Piadas Ruins'),
        ('PUBLICAS' , 'Publicas'),
        ('OUTROS', 'Outros'),
    )
    pessoa = models.ForeignKey(
        Pessoa, on_delete = None
    )

    titulo = models.CharField(
        max_length = 255,
        verbose_name = 'Nome de ideia',
        unique = True
    )
    descricao = models.TextField(
        verbose_name='Descreva sua ideia'
    )

    categorias = models.CharField(
        max_length = 255,
        verbose_name = 'Categorias',
        choices = CATEGORIAS
    )
    categorias_outros = models.CharField(
        null = True,
        blank = True,
        max_length = 255,
        verbose_name = 'Caso outros, qual?'
    )

    data_de_criacao = models.DateTimeField(auto_now_add = True)
    data_de_atualizacao = models.DateTimeField(auto_now = True)
    ativo = models.BooleanField(default=True)

    def __str__ (self):
        return self.pessoa.nome + ' ' + self.titulo