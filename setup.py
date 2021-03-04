from setuptools import setup, find_packages

version = __import__('runapscheduler').__version__

setup(
    name='django-runapscheduler',
    version=version,
    description='Command for standalone apscheduler jobs',
    author='DevForth',
    author_email='contact@devforth.io',
    url='http://github.com/devforth/django-runapscheduler',
    packages=find_packages(exclude=['ez_setup']),
    include_package_data=True,
    install_requires=open('requirements.txt').read().splitlines(),
    zip_safe=True,
)