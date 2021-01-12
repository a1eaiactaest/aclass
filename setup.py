#!/usr/bin/env python3

import os
from setuptools import setup

directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(direcory, 'README.md'), encoding='utf-8') as f:
  long_description = f.read()


setup(name='aclass',
      version='0.0.1',
      description='Online Classes Automation',
      author='Piotrek Rybiec',
      license='MIT',
      long_description=long_description,
      long_description_content_type='text/markdown',
      packages=['aclass'],
      classifires=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
      ],
      url='url',
      install_requires=[INSERT SOMETHING],
      entry_points={
        "console_scripts":[
          "azoom=azoom.__main__:main",
        ]
      },
      include_package_data=True)
