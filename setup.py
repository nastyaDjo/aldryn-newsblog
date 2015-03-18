# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from aldryn_newsblog import __version__

REQUIREMENTS = [
    'backport_collections==0.1',
    'django-parler',
    'django-filer>=0.9.9,<0.10',
    'aldryn-common',
    'django-appdata>=0.1.4',
    'django-cms>=3.0.12',
    'aldryn-people>=0.4.6',
    'django>=1.6,<1.8',
    'aldryn-apphooks-config>=0.1.4',
    'django-reversion>=1.8.2,<1.9',
    'django-taggit',
    'aldryn-boilerplates',
    'aldryn-categories',
    'aldryn-reversion',
    'six',
    'pytz',
    'django-sortedm2m',
]

CLASSIFIERS = [
    'Development Status :: 2 - Pre-Alpha',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
]

setup(
    name='aldryn-newsblog',
    version=__version__,
    description='Adds blogging and newsing capabilities to django CMS',
    author='Divio AG',
    author_email='info@divio.ch',
    url='https://github.com/aldryn/aldryn-newsblog',
    packages=find_packages(),
    license='LICENSE.txt',
    platforms=['OS Independent'],
    install_requires=REQUIREMENTS,
    classifiers=CLASSIFIERS,
    include_package_data=True,
    zip_safe=False,
    test_suite="test_settings.run",
)
