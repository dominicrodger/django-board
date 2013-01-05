from setuptools import setup, find_packages

import board

setup(
    name='django-board',
    version=board.__version__,
    description='A Django app for managing an organisation\'s board members page.',
    long_description=open('README.rst').read(),
    author='Dominic Rodger',
    author_email='internet@dominicrodger.com',
    url='http://github.com/dominicrodger/django-board',
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
    package_data={'': ['README.rst']},
    zip_safe=False,
    install_requires=[
        'Django==1.4.3',
        'sorl-thumbnail==11.12',
        'PIL==1.1.7',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'License :: OSI Approved :: BSD License',
    ],
    tests_require=(
        'django-setuptest==0.1.2',
        'factory_boy==1.2.0',
    ),
    test_suite='setuptest.setuptest.SetupTestSuite',
)
