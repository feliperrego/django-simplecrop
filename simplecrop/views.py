#-*- coding: utf-8 -*-
import os
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.http import HttpResponse
from django.utils import simplejson
from django.views.decorators.csrf import csrf_exempt
from PIL import ImageOps, Image
from django.conf import settings


def crop_view(request):
    lista = {}
    for post in request.POST:
        try:
            parametro = post.split("_._._")[0]
            path = post.split("_._._")[1]
            cropName = "%sx%s" % (post.split("_._._")[2], post.split("_._._")[3])
            if lista.has_key(path):
                if lista[path].has_key(cropName):
                    lista[path][cropName].update({parametro: request.POST.get(post)})
                else:
                    lista[path].update({cropName: {parametro: request.POST.get(post)}})
            else:
                lista.update({path: {cropName: {parametro: request.POST.get(post)}}})
        except:
            pass

    for imagem_path in lista:
        if not os.path.exists("%s/%s/thumbs/" % (settings.MEDIA_ROOT, os.path.dirname(imagem_path))):
            os.mkdir("%s/%s/thumbs/" % (settings.MEDIA_ROOT, os.path.dirname(imagem_path)))

        #Admin Thumb
        image = Image.open("%s/%s" % (settings.MEDIA_ROOT, imagem_path))
        thumb = ImageOps.fit(image, (105, 105), Image.ANTIALIAS)
        thumb.save("%s/%s/thumbs/105x105_%s" % (settings.MEDIA_ROOT, os.path.dirname(imagem_path), os.path.basename(imagem_path)))

        #Others Thumbs
        for crop in lista[imagem_path]:
            image = Image.open("%s/%s" % (settings.MEDIA_ROOT, imagem_path))

            x1 = int((image.size[0] / float(lista[imagem_path][crop]['w'])) * float(lista[imagem_path][crop]['x1']))
            x2 = int((image.size[0] / float(lista[imagem_path][crop]['w'])) * float(lista[imagem_path][crop]['x2']))
            y1 = int((image.size[1] / float(lista[imagem_path][crop]['h'])) * float(lista[imagem_path][crop]['y1']))
            y2 = int((image.size[1] / float(lista[imagem_path][crop]['h'])) * float(lista[imagem_path][crop]['y2']))

            dimensao = (x1, y1, x2, y2)
            imagem_crop = image.crop(dimensao)
            imagem_crop = ImageOps.fit(imagem_crop, (int(crop.split("x")[0]), int(crop.split("x")[1])), Image.ANTIALIAS)
            imagem_crop.save("%s/%s/thumbs/%s_%s" % (settings.MEDIA_ROOT, os.path.dirname(imagem_path), crop, os.path.basename(imagem_path)), image.format, quality=100)

    if request.is_ajax():
        return HttpResponse(simplejson.dumps({"sucesso": True}))


@csrf_exempt
def upload_view(request):
    this_file = request.FILES['file']
    default_storage.save("%s/teste/%s" % (settings.MEDIA_ROOT, this_file), ContentFile(this_file.read()))
    path_image = "%steste/%s" % (settings.MEDIA_URL, this_file)
    return HttpResponse(path_image)