import os
from setuptools import setup


def read(fname):
    """Utility function to read the README file.

    Used for long_description. It's nice, because now (1) we have a top level
    README file and (2) it's easier to type in the README file than to put a raw
    string in below."""
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="ipycache",
    version="0.1.5tev",
    author="Cyrille Rossant",
    author_email="rossant@github",
    description=("Defines a %%cache cell magic in the IPython notebook to "
                 "cache results of long-lasting computations in a persistent "
                 "pickle file."),
    license="BSD-3-Clause",
    keywords="ipython notebook cache",
    url="https://github.com/rossant/ipycache",
    py_modules=['ipycache'],
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "Framework :: IPython",
        "License :: OSI Approved :: BSD License",
    ],
)
