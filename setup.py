#-*- coding: utf-8 -*-
from glob import glob
from setuptools import setup, find_packages
#from distutils.core import setup

setup(
    name='django-simplecrop',
    version='beta',
    packages=find_packages(),
    url='https://github.com/feliperrego/django-simplecrop',
    license='BSD',
    author=u'Felipe R. Rêgo',
    author_email='feliperrego@gmail.com',
    description='A simple module to make easier crop images in Django admin.',
    long_description=open('README.md').read(),
    include_package_data=True,
    data_files = [('static', glob('./simplecrop/static/*'))],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3'
    ],
    zip_safe = False,
)