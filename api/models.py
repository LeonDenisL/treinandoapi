from django.db import models

class Oficio(models.Model):
    cabecalho = models.CharField(max_length=275)
    paragrafo_um = models.CharField(max_length=500)
    paragrafo_dois = models.CharField(max_length=500)
    rodape = models.CharField(max_length=250)
    endereco = models.CharField(max_length=250)
    telefone = models.CharField(max_length=15)

    class Meta:
        verbose_name = 'Oficio'
        verbose_name_plural = 'Oficios'

    def __str__(self):
        return self.cabecalho

