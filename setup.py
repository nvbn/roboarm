from setuptools import setup, find_packages
import sys, os

version = '1.0'

setup(name='roboarm',
      version=version,
      description="Python library for controlling owi robotic arm edge",
      long_description=open('README.rst').read(),
      classifiers=[
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
      ], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Vladimir Iakovlev',
      author_email='nvbn.rm@gmail.com',
      url='https://github.com/nvbn/roboarm',
      license='BSD',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          'pyusb',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
