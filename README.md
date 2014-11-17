
django-simplecrop
================

Simple module to make easier crop images in Django admin.


Installation
-----------------------------------
Install ``django-simplecrop`` (or download from [PyPI](http://pypi.python.org/pypi/django-simplecrop/ "Download from PyPI")):

    pip install django-simplecrop

Add ``simplecrop`` to ``INSTALLED_APPS`` in ``settings.py``:


    INSTALLED_APPS = (
        ...
        'simplecrop',
        ...
    )
    
Include ``simpleCropAutodiscover()`` after ``admin.autodiscover()``:
    
    ...
    from simplecrop.utils import simpleCropAutodiscover
    
    admin.autodiscover()
    simpleCropAutodiscover()

Include ``simplecrop.urls`` in ``urls.py``:
    
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
Step 1 - Add image:
![Step 1](http://feliperego.com/img/step1.png "Step 1")

Step 2 - Crop images:
![Step 2](http://feliperego.com/img/step2.png "Step 2")


Authors
-----------------

- [Felipe R. Rêgo](https://github.com/feliperrego "GitHub - Felipe R. Rêgo")
- [Silvio Lucena Junior](https://github.com/silviolucenajunior "GitHub - Silvio Lucena")
