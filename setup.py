# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

setup(
    name='cmsplugin-feed-ai',
    version='0.0.1',
    author='Anders Innovations',
    author_email='info@anders.fi',
    packages=find_packages(
        exclude=[
            "tests",
        ]
    ),
    include_package_data=True,
    license='MIT',
    description='Social media feed plugin for Django CMS',
    install_requires=[
        'django-cms>=3.2,<3.4',
    ],
    url='https://github.com/andersinno/cmsplugin-feed-ai',
)
