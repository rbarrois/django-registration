import os
from setuptools import setup

from registration import get_version


setup(name='django-registration',
      version='0.8.1-alpha1',
      description='An extensible user-registration application for Django',
      author='James Bennett',
      author_email='james@b-list.org',
      url='http://www.bitbucket.org/ubernostrum/django-registration/wiki/',
      download_url='http://www.bitbucket.org/ubernostrum/django-registration/get/v0.7.gz',
      install_requires = ['django >=1.3'],
      packages=['registration'],
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Web Environment',
          'Framework :: Django',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: Utilities',
      ],
      test_suite='registration_tests.runner.runtests',
)
