# monkey patch from
# http://old.nabble.com/problem-with-numpy.distutils-and-Cython-td25100957.html
from numpy.distutils.command import build_src
import Cython
import Cython.Compiler.Main
build_src.Pyrex = Cython
build_src.have_pyrex = True
