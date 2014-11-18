#-*- coding: utf-8 -*-
from setuptools import setup, find_packages
import simplecrop

version = simplecrop.__version__

setup(
    name='django-simplecrop',
    version=version,
    description='A simple module to make easier crop images in Django admin.',
    long_description=open('README.md').read(),
    install_requires=[
        "django",
        "PIL"
    ],
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
        "Environment :: Web Environment",
    ],
    keywords='crop,django',
    author=u'Felipe R. Rêgo',
    author_email='feliperrego@gmail.com',
    url='https://github.com/feliperrego/django-simplecrop',
    license='BSD',
    packages=find_packages(),
    package_data = {
        'simplecrop': [
            'templates/simpleCrop/*.html',
            'static/simplecrop/css/*.css',
            'static/simplecrop/img/*.gif',
            'static/simplecrop/js/*.js'
        ],
    },
    include_package_data=True,
    zip_safe = False,
)