import sys, os, numpy as np
import glob
from setuptools import setup, Extension
from Cython.Build import cythonize

# Changing the working directory to where this script is to run from anywhere.
os.chdir(os.path.dirname(__file__))

# Forcing all the source files to be recompiled.
os.environ["CYTHON_FORCE_REGEN"] = "1" if "--force" in sys.argv else "0"


ENABLE_PROFILING = False
"""
Specify whether to enable profiling or not. Note that profiling cause a slight overhead to each function call.
See https://cython.readthedocs.io/en/latest/src/tutorial/profiling_tutorial.html for more information.
"""

if "--profile" in sys.argv:
    ENABLE_PROFILING = True
    sys.argv.remove("--profile")

USE_CYTHON = 1
"""
Specify whether to use `Cython` to build the extensions from the `.pxd` files or use the already generated `.c`/`.cpp` files:

- Set it to `1` to enable building extensions using Cython.
- Set it to `0` to build extensions from the `.c`/`.cpp` files.
- Set it to `-1` to build with Cython if available, otherwise from the C file.
"""

# Source: https://stackoverflow.com/questions/28301931/how-to-profile-cython-functions-line-by-line
if ENABLE_PROFILING:
    from Cython.Compiler.Options import get_directive_defaults
    
    directive_defaults = get_directive_defaults()
    directive_defaults['linetrace'] = True
    directive_defaults['binding'] = True


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
PackageName = "PackageName"

packages = [PackageName]

python_packages = [os.path.dirname(module).replace("src", "PackageName").replace(os.path.sep, ".") for module in glob.glob("src/**/*.py", recursive=True) if not os.path.dirname(module) == "src"]

packages.extend(python_packages)

if sys.version_info[0] == 2:
    raise Exception("Python 2.x is not supported")

if USE_CYTHON:
    cython_extensions = glob.glob("src/**/*.pyx", recursive=True)
    cmdclass.update({ "build_ext": build_ext })
else:
    cython_extensions = glob.glob("src/**/*.c", recursive=True)
    cython_extensions += glob.glob("src/**/*.cpp", recursive=True)


# Creating the C extensions.
for extension_full_path in cython_extensions:
    ext_relpath = os.path.splitext(os.path.relpath(extension_full_path))
    
    ext_fullname = ext_relpath[0].replace("src", PackageName, 1)
    
    packages.append(os.path.dirname(ext_fullname).replace(os.path.sep, "."))
    
    ext_fullname = ext_fullname.replace(os.path.sep, ".")
    
    ext_modules.append(Extension(
        name = ext_fullname,
        sources = [f"{ext_relpath[0]}{ext_relpath[1]}"],
        extra_compile_args=["/openmp"], # Comment this if you don't want to use OpenMP.
        extra_link_args=['/openmp'],    # Comment this if you don't want to use OpenMP.
        define_macros= [("CYTHON_TRACE", "1")] if ENABLE_PROFILING else [ ] + 
                       [('NPY_NO_DEPRECATED_API', 'NPY_1_7_API_VERSION')] # Comment this if you don't want to use NumPy.
    ))


# Removing duplicates from the list of packages.
packages = list(set(packages))

# https://stackoverflow.com/questions/58533084/what-keyword-arguments-does-setuptools-setup-accept
setup(
    packages=packages,
    cmdclass = cmdclass,
    ext_modules=cythonize(ext_modules, language_level=3),
    include_dirs=[np.get_include()], # Comment this if you don't want to use NumPy.
)
