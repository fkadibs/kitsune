from setuptools import setup

setup(
  name = 'kitsune',
  version = '0.0.2',
  author = 'disaster_byte',
  install_requires = ['fonttools'],
  packages = ['kitsune'],
  entry_points = {
    'console_scripts': [
      'kitsune = kitsune.kitsune:main'
    ],
  },
 )
