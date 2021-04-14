from distutils.core import setup
from setuptools import find_packages

setup(
    name="django-unicorn",
    version="0.26.0",
    description="A magical full-stack framework for Django.",
    authors=["Adam Hill <unicorn@adamghill.com>"],
    license="MIT",
    readme="README.md",
    repository="https://github.com/adamghill/django-unicorn/",
    homepage="https://www.django-unicorn.com",
    keywords=["django", "python", "javascript", "fullstack"],
    install_requires=[
        "django>=2.2",
        "beautifulsoup4>=4.8.0",
        "orjson==3.2.1",
        "shortuuid==1.0.1",
        "cachetools==4.1.1",
        "dataclasses==0.8.0",
        "decorator==4.4.2",
    ],
)
