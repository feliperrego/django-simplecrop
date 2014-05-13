#-*- coding: utf-8 -*-
import os
from django.conf import settings
from django.shortcuts import render_to_response, HttpResponseRedirect
from django.template import RequestContext
from django.db.models import signals
from django.contrib import admin


class MyImage():
    """Classe utilizada para organizar as imagens passadas para a view de crop de imagens."""
    name = None
    path = None
    crops = []

    def __init__(self, name, path, crops):
        self.name = name
        self.path = path
        self.crops = crops

    def getCrops(self):
        crops = []
        for crop in self.crops:
            crops.append((crop.split("x")[0], crop.split("x")[1]))
        return crops

    def getCropTotal(self):
        return len(self.crops)


def post_delete(signal, instance, sender, **kwargs):
    """Signal para excluir thumbnails geradas em um model."""
    instance.deletar_miniaturas()


def deletar_miniaturas(self):
    """Função chamada na signal para excluir thumbnails"""
    for thumb in self.__crops__:
        imagem = self.__getattribute__(thumb[0]).name

        try:
            os.unlink("%s/%s" % (settings.MEDIA_ROOT, imagem))
            os.unlink("%s/%s/thumbs/105x105_%s" % (settings.MEDIA_ROOT, os.path.dirname(imagem), os.path.basename(imagem)))
        except:
            pass

        for crop in thumb[1]:
            try:
                os.unlink("%s/%s/thumbs/%s_%s" % (settings.MEDIA_ROOT, os.path.dirname(imagem), crop, os.path.basename(imagem)))
            except:
                pass


def render_crop(request, redirect, obj):
    """
        Renderiza o html de crop de imagens após um modulo ser salvo, é necessário existir o parametro "__crop__"
        especificado no modelo.
    """
    totalCrops = 0
    imagens = []
    crops = obj.__crops__
    for crop in crops:
        newImage = MyImage(crop[0], obj.__getattribute__(crop[0]).name, crop[1])
        imagens.append(newImage)
        totalCrops += newImage.getCropTotal()

    variaveis = RequestContext(request, {"redirect": redirect, "imagens": imagens, "totalCrops": totalCrops})
    return render_to_response('simpleCrop/crop.html', variaveis)


def simpleCropAutodiscover():
    """
        Função chamada em urls.py depois de "admin.autodiscover()" para implementar automaticamente a chamada das
        funções de criar as thumbnails dos modulos que tenham o atributo "__crop__".
    """
    site = admin.site
    for model, model_admin in site._registry.items():

        if hasattr(model, "__crops__"):

            setattr(model, "deletar_miniaturas", deletar_miniaturas)
            signals.pre_delete.connect(post_delete, sender=model)

            class CropAdmin(model_admin.__class__):
                def response_add(self, request, obj):
                    if request.POST.has_key("_continue"):
                        redirect = "../%s" % obj.id
                    elif request.POST.has_key("_addanother"):
                        redirect = ""
                    else:
                        redirect = "../"
                    return render_crop(request, redirect, obj)

                def response_change(self, request, obj):
                    if request.POST.has_key("_continue"):
                        redirect = "../%s" % obj.id
                    elif request.POST.has_key("_addanother"):
                        redirect = ""
                    else:
                        redirect = "../"
                    for crop in obj.__crops__:
                        if request.FILES.has_key(crop[0]):
                            return render_crop(request, redirect, obj)
                        else:
                            return HttpResponseRedirect(redirect)

            site.unregister(model)
            site.register(model, CropAdmin)