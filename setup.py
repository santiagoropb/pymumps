#!/usr/bin/env python

from setuptools import setup, Extension
import sys

try:
    import Cython
except ImportError:
    raise ImportError('''
Cython is required for building this package. Please install using

    pip install cython

or upgrade to a recent PIP release.
''')


with open('README.md') as f:
    long_description = f.read()

include_dirs = None
if '--include-dirs' in sys.argv:
    index = sys.argv.index('--include-dirs')
    sys.argv.pop(index)
    include_dirs = [sys.argv.pop(index)]
    
library_dirs = None
if '--library-dirs' in sys.argv:
    index = sys.argv.index('--library-dirs')
    sys.argv.pop(index)
    library_dirs = [sys.argv.pop(index)]

print(library_dirs)
print(include_dirs)
    
setup(
    name='PyMUMPS',
    version='0.3.2',
    description='Python bindings for MUMPS, a parallel sparse direct solver',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Bradley M. Froehle',
    author_email='brad.froehle@gmail.com',
    maintainer='Stephan Rave',
    maintainer_email='stephan.rave@uni-muenster.de',
    license='BSD',
    url='http://github.com/pymumps/pymumps',
    packages=['mumps'],
    ext_modules=[
        Extension(
            'mumps._dmumps',
            sources=['mumps/_dmumps.pyx'],
            libraries=['dmumps', 'mumps_common', 'esmumps', 'metis', 'scotch', 'openblas', 'mpiseq', 'pord'],
            include_dirs=include_dirs,
            library_dirs=library_dirs
        ),
    ],
    install_requires=['mpi4py'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Mathematics',
    ],
)
