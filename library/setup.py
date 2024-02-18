from setuptools import setup, find_packages


classifiers = ['Development Status :: 4 - Beta',
               'Operating System :: POSIX :: Linux',
               'License :: OSI Approved :: MIT License',
               'Intended Audience :: Developers',
               'Programming Language :: Python :: 2.7',
               'Programming Language :: Python :: 3',
               'Topic :: Software Development',
               'Topic :: System :: Hardware']

setup(name='ST7789',
      version='0.0.4',
      description='Library to control ST7789 TFT LCD displays.',
      long_description=open('README.md').read(),
      long_description_content_type='text/markdown',
      license='MIT',
      author='Benedikt Priller',
      author_email='benedikt.priller@pri-os.de',
      classifiers=classifiers,
      url='https://github.com/Benedikt-Priller/display-st7789-python/',
      packages=find_packages())
