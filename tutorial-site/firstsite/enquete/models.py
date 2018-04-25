from django.db import models


class Pergunta(models.Model):
    pergunta_texto = models.CharField(max_length=255)
    data_publicacao = models.DateTimeField('Data de publicação')

    def __str__(self):
        return self.pergunta_texto


class Opcao(models.Model):
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    texto = models.CharField(max_length=255)
    votacoes = models.IntegerField(default=0)

    def __str__(self):
        return self.texto
