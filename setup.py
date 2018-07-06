import os
import sys
from setuptools import setup

if sys.version_info < (3, 0):
    sys.exit('Sorry, Python < 3.0 is not supported')

REQUIRED_PACKAGES = ['numpy', 'pywavelets', 'numba']

setup(name='sigpy',
      version='0.1',
      description='Python package for signal reconstruction.',
      url='http://github.com/mikgroup/sigpy',
      author='Frank Ong',
      author_email='frankong@berkeley.edu',
      license='BSD',
      packages=['sigpy'],
      install_requires=REQUIRED_PACKAGES,
      scripts=['bin/sigpy_plot'],
      zip_safe=False)