import setuptools
from setuptools import setup

setup(
    name='seq2label',
    version='0.0.1',
    packages=setuptools.find_packages(),
    url='',
    include_package_data=True,
    license='MIT',
    author='Xiaoquan Kong',
    author_email='u1mail2me@gmail.com',
    description='seq2label',
    install_requires=['tensorflow', 'flask', 'flask-cors', 'ioflow']
)
