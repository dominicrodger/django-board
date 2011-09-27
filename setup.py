from setuptools import setup

setup(
    name='django-board',
    version='0.1.0',
    description='A Django app for managing an organisation\'s board members page.',
    long_description=open('README.md').read(),
    author='Dominic Rodger',
    author_email='internet@dominicrodger.com',
    url='http://github.com/dominicrodger/django-board',
    license='BSD',
    packages=['board'],
    include_package_data=True,
    package_data={'': ['README.md']},
    zip_safe=False,
    install_requires=['Django', 'South', 'sorl-thumbnail',]
)
