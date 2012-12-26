from distutils.core import setup
import os

## generate list of all sub-packages
subdirs = [i[0].split(os.path.sep)[1:] for i in os.walk('./pyqtgraph') if '__init__.py' in i[2]]
subdirs = filter(lambda p: len(p) == 1 or p[1] != 'build', subdirs)
all_packages = ['.'.join(p) for p in subdirs] + ['pyqtgraph.examples']

setup(name='pyqtgraph',
    version='',
    description='Scientific Graphics and GUI Library for Python',
    long_description="""\
PyQtGraph is a pure-python graphics and GUI library built on PyQt4/PySide and numpy. 

It is intended for use in mathematics / scientific / engineering applications. Despite being written entirely in python, the library is very fast due to its heavy leverage of numpy for number crunching, Qt's GraphicsView framework for 2D display, and OpenGL for 3D display.
""",
    license='MIT',
    url='http://www.pyqtgraph.org',
    author='Luke Campagnola',
    author_email='luke.campagnola@gmail.com',
    packages=all_packages,
    package_dir={'pyqtgraph.examples': 'examples'},  ## install examples along with the rest of the source
    #package_data={'pyqtgraph': ['graphicsItems/PlotItem/*.png']},
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "Environment :: Other Environment",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Visualization",
        "Topic :: Software Development :: User Interfaces",
        ],
    requires = [
        'numpy',
        'scipy',
        ],
)

