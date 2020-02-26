from setuptools import setup

setup(
  name = 'kitsune',
  version = '0.0.1',
  author = 'disaster_byte',
  packages = ['kitsune'],
  entry_points = {
    'console_scripts': [
      'kitsune = kitsune.kitsune:main'
    ],
  },
 )
