#-*-coding: utf-8 -*-
__version__ = "1.0.4"

try:
    from django.template import add_to_builtins
    add_to_builtins("simplecrop.template_tags")
except:
    pass