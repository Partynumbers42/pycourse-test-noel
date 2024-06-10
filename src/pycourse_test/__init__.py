"""Demo package for course"""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("pycourse-test-noel")
except PackageNotFoundError:
    __version__ = "uninstalled"
__author__ = "F. Noel"
__email__ = "test@test.com"
