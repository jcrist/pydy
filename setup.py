#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from setuptools import setup, find_packages

exec(open('pydy/version.py').read())

# I was getting the same error as:
# https://github.com/statsmodels/statsmodels/issues/1073, so the following
# line is added.
os.environ["MPLCONFIGDIR"] = "."

setup(
    name='pydy',
    version=__version__,
    author='PyDy Authors',
    author_email='pydy@googlegroups.com',
    url="http://pydy.org",
    description='Python tool kit for multi-body dynamics.',
    long_description=open('README.rst').read(),
    keywords="multibody dynamics",
    license='LICENSE.txt',
    packages=find_packages(),
    install_requires=['sympy>=0.7.4.1',
                      'numpy>=1.7',
                      'scipy>=0.11',
                      ],
    extras_require={'doc': ['sphinx', 'numpydoc'],
                    'codegen': ['Cython>=0.17', 'Theano>=0.6.0'],
                    'examples': ['matplotlib>=0.99'],
                    },
    tests_require=['nose>=1.3.0'],
    test_suite='nose.collector',
    scripts=['bin/benchmark_pydy_code_gen.py'],
    include_package_data=True,
    classifiers=['Development Status :: 4 - Beta',
                 'Intended Audience :: Science/Research',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python :: 2.7',
                 'Topic :: Scientific/Engineering :: Physics',
                 ],
)
