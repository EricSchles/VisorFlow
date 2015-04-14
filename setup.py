#!/usr/bin/env python

######################################################################
# Copyright (C) 2011,2012,2014 Jaakko Luttinen
#
# This file is licensed under Version 3.0 of the GNU General Public
# License. See LICENSE for a text of the license.
######################################################################

######################################################################
# This file is part of BayesPy.
#
# BayesPy is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License version 3 as
# published by the Free Software Foundation.
#
# BayesPy is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with BayesPy.  If not, see <http://www.gnu.org/licenses/>.
######################################################################

NAME         = 'SoundVolt'
DESCRIPTION  = 'Music stat tools for Python'
AUTHOR       = 'Vishal Lall'
AUTHOR_EMAIL = 'vishalhlall@gmail.com'
URL          = 'http://vishallall.com/soundvolt'
LICENSE      = 'GPLv3'
VERSION      = '0.1'

if __name__ == "__main__":

    import os

    # Utility function to read the README file.
    # Used for the long_description.  It's nice, because now 1) we have a top level
    # README file and 2) it's easier to type in the README file than to put a raw
    # string in below ...
    def read(fname):
        return open(os.path.join(os.path.dirname(__file__), fname)).read()

    from setuptools import setup, find_packages
    
    # Setup for BayesPy
    setup(
          install_requires = ['numpy>=1.8.0', # 1.8 implements broadcasting in numpy.linalg
                              'scipy>=0.13.0', # <0.13 have a bug in special.multigammaln
                              'matplotlib>=1.2.0'],
          
          packages         = find_packages(),
          package_data     = {NAME: ["tests/baseline_images/test_plot/*.png"]},
          name             = NAME,
          version          = VERSION,
          author           = AUTHOR,
          author_email     = AUTHOR_EMAIL,
          description      = DESCRIPTION,
          license          = LICENSE,
          url              = URL,
          keywords         =
            [
              'variational Bayes',
              'probabilistic programming',
              'Bayesian networks',
              'graphical models',
              'variational message passing'
            ],
          classifiers =
            [ 
              'Programming Language :: Python :: 3 :: Only',
              'Programming Language :: Python :: 3.3',
              'Programming Language :: Python :: 3.4',
              'Development Status :: 4 - Beta',
              'Environment :: Console',
              'Intended Audience :: Developers',
              'Intended Audience :: Science/Research',
              'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
              'Operating System :: OS Independent',
              'Topic :: Scientific/Engineering',
              'Topic :: Scientific/Engineering :: Information Analysis'
            ]
          )
