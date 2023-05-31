import sys, os, numpy as np
import glob
from setuptools import setup, Extension

os.chdir(os.path.dirname(__file__))

# Forcing the cython files to be recompiled regardless of modification times and changes.
os.environ["CYTHON_FORCE_REGEN"] = "1" if "--force" in sys.argv else "0"

USE_CYTHON = 1
"""
Specify whether to use `Cython` to build the extensions or use the `C` files (that were previously generated with Cython):

- Set it to `1` to enable building extensions using Cython.
- Set it to `0` to build extensions from the C files (that were previously generated with Cython).
- Set it to `-1` to build with Cython if available, otherwise from the C file.
"""

if USE_CYTHON:
    try:
        from Cython.Distutils import build_ext
    except ImportError:
        if USE_CYTHON == -1:
            USE_CYTHON = 0
        else:
            raise

cmdclass = { }
"""Dictionary of commands to pass to setuptools.setup()"""

ext_modules = [ ]
"""List of extension modules to pass to setuptools.setup()"""

# Modify the PackageName to the name of your package.
packages = ["PackageName", "PackageName.extensions"]

if sys.version_info[0] == 2:
    raise Exception("Python 2.x is not supported")

if USE_CYTHON:
    cython_extensions = glob.glob("src/extensions/**/*.pyx", recursive=True)
    cmdclass.update({ "build_ext": build_ext })
else:
    cython_extensions = glob.glob("src/extensions/**/*.c", recursive=True)

for extension_path in cython_extensions:
    ext_filename = os.path.splitext(os.path.basename(extension_path))
    
    # Also put you package name here.
    packages.append("PackageName.extensions." + ext_filename[0])
    
    # Here too.
    ext_modules.append(Extension(
        name = f"PackageName.extensions.{ext_filename[0]}.{ext_filename[0]}",
        sources = [f"src/extensions/{ext_filename[0]}/{ext_filename[0]}{ext_filename[1]}"],
        # extra_compile_args=["/openmp"], # Remove this if you don't want to use OpenMP.
        # extra_link_args=['/openmp'],    # Remove this if you don't want to use OpenMP.
        define_macros=[('NPY_NO_DEPRECATED_API', 'NPY_1_7_API_VERSION')] # Remove this if you don't want to use NumPy.
    ))

# https://stackoverflow.com/questions/58533084/what-keyword-arguments-does-setuptools-setup-accept
setup(
    packages=packages,
    cmdclass = cmdclass,
    ext_modules=ext_modules,
    include_dirs=[np.get_include()],
)
