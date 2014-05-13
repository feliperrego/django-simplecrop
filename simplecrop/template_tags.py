from PIL import Image, ImageOps
from django import template
import os
from django.conf import settings


register = template.Library()


def thumbnail(foto, tamanho):
    nome = os.path.basename(foto.name)
    dir = os.path.dirname(foto.name)

    if not os.path.exists("%s/%s/thumbs/%s_%s" % (settings.MEDIA_ROOT, dir, tamanho, nome)):
        if not os.path.exists("%s/%s/thumbs/" % (settings.MEDIA_ROOT, dir)):
            os.mkdir("%s/%s/thumbs/" % (settings.MEDIA_ROOT, dir))
        size = (int(tamanho.split("x")[0]), int(tamanho.split("x")[1]))
        try:
            image = Image.open("%s/%s" % (settings.MEDIA_ROOT, nome))
        except:
            image = Image.open("%s/%s" % (settings.MEDIA_ROOT, foto.name))
        thumb = ImageOps.fit(image, size, Image.ANTIALIAS)
        thumb.save("%s/%s/thumbs/%s_%s" % (settings.MEDIA_ROOT, dir, tamanho, nome), quality=99)
    return "%s%s/thumbs/%s_%s" % (settings.MEDIA_URL, dir, tamanho, nome)
register.simple_tag(thumbnail)