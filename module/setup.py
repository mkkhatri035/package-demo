from setuptools import setup, find_packages
from demo_package import __version__ , __name__

DESCRIPTION = __name__
LONG_DESCRIPTION = f'This is {__name__} package'

with open("README.md", encoding="utf8") as f:
    long_description = f.read()

setup(
    name=__name__,
    version=__version__,
    author="<author>",
    author_email="<author@example.com>",
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=["numpy>=1.20.3"],
    zip_safe=False,
    python_requires='>=3.6',
)