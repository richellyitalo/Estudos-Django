from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Título')
    subtitle = models.CharField(max_length=255, null=True, blank=True, verbose_name='Subtítulo')
    content = models.TextField(verbose_name='Conteúdo')

    class Meta:
        verbose_name = 'Artigo'
        # verbose_name_plural = 'Artigos'

    def __str__(self):
        return self.title
