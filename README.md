
django-simplecrop
================

Simple module to make easier crop images in Django admin.


Installation
-----------------------------------
Install ``django-simplecrop`` (or `download from [PyPI](http://pypi.python.org/pypi/django-simplecrop/ "Download from PyPI")):

    pip install django-simplecrop

Add ``simplecrop`` to ``INSTALLED_APPS`` in ``settings.py``:


    INSTALLED_APPS = (
        ...
        "simplecrop",
        ...
    )
    
Inlclude ``simpleCropAutodiscover()`` after ``admin.autodiscover()``:
    
    ...
    from simplecrop.utils import simpleCropAutodiscover
    
    admin.autodiscover()
    simpleCropAutodiscover()

Include ``simplecrop.urls`` in your ``urls.py``:
    
    urlpatterns = patterns('',
        ...
        url(r'^simplecrop/', include('simplecrop.urls')),
    )
    
    
Usage
------------------


Include the ``__crops__`` parameter in your model and specify the field and image sizes:

    class MyModel(models.Model):
        __crops__ = [
            ["image", ["110x110", "200x150"]]
        ]

        title = models.CharField(u"Title", max_length=128)
        text = models.TextField("Text")
        image = models.ImageField("Image", upload_to="images")


Testing
-----------------
Step 1 - Add an image to your model and click the save button:
![Step 1](https://photos-5.dropbox.com/t/0/AAAbIUFlisdivxlOS9JDtjHu0oe_UcGpA2lWEEjWy9PZLg/12/35856195/png/2048x1536/3/1400014800/0/2/step1.png/msi85fl_eYtFqadIi39FbX_GdXJ6opfyYP3a1cYDgg0 "Step 1")

Step 2 - Crop images:
![Step 2](https://photos-1.dropbox.com/t/0/AACww3yrcYeWZLtcHiRlGaHB4vWieIuwW5i0hJ6y_CJ_8Q/12/35856195/png/2048x1536/3/1400014800/0/2/step2.png/D0k4WZUl5QSkmTspbklNr9LGpTJyV1WgjoX7EPxBInA "Step 2")


Authors
-----------------

- [Felipe R. Rêgo](https://github.com/feliperrego "GitHub - Felipe R. Rêgo")
- [Silvio Lucena Jr.](https://github.com/feliperrego "GitHub - Silvio Lucena")