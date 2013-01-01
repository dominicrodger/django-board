from setuptools import setup, find_packages

import board

setup(
    name='django-board',
    version=board.__version__,
    description='A Django app for managing an organisation\'s board members page.',
    long_description=open('README.md').read(),
    author='Dominic Rodger',
    author_email='internet@dominicrodger.com',
    url='http://github.com/dominicrodger/django-board',
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
    package_data={'': ['README.md']},
    zip_safe=False,
    install_requires=[
        'Django==1.4.3',
        'South==0.76',
        'sorl-thumbnail==11.12',
    ]
)
