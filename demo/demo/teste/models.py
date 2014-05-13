#-*- coding: utf-8 -*-
from django.db import models

class Noticia(models.Model):
    __crops__ = [
        ["imagem", ["110x110", "750x615"]]
    ]

    titulo = models.CharField(u"Title", max_length=128)
    texto = models.TextField("Text")
    imagem = models.ImageField("Image", upload_to="noticia/imagens")

    class Meta:
        verbose_name = u"MyModel"
        verbose_name_plural = u"MyModel"

    def __unicode__(self):
        return self.titulo

    def __str__(self):
        return self.titulo