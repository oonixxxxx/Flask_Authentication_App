from setuptools import setup, find_packages

setup(
    name="onixhub",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        'Flask==3.0.2',
        'Flask-SQLAlchemy==3.1.1',
        'Flask-Migrate==4.0.5',
        'Flask-Caching==2.1.0',
        'Flask-JWT-Extended==4.6.0',
    ]
) 