from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
from Cython.Build import cythonize
from numpy import get_include
from os import system

shared_obj = "gcc -fPIC -O3 -c csum.c -o csum.o"
print shared_obj
system(shared_obj)

"""
ext_modules = [Extension(
                        "cython_csum",
                        ["cython_csum.pyx"],
                        extra_compile_args=["-fPIC", "-O3"],
                        extra_link_args=["csum.o"])]
"""
setup(name = "cython_csum",
    ext_modules = cythonize([Extension("cython_csum", ["cython_csum.pyx"], extra_link_args=["csum.o"])]))
