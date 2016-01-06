from distutils.core import setup
from Cython.Build import cythonize

setup(name="cysum", ext_modules=cythonize("cysum.pyx"))
