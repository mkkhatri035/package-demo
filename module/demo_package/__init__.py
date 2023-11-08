"""This is the main module."""

from .functions import (Add, Subtract)
from . import sub_module

__name__="demov_package"

__version__="0.0.1"

__all__=[
    "Add",
    "Subtract",
    "sub_module"
]