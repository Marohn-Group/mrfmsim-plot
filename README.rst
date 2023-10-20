mrfmsim-plot
=============

This module provides scripts for generating plots for magnetic resonance force microscopy experiments. It serves as a plugin library for the `mrfmsim repository <https://github.com/Marohn-Group/mrfmsim>`_ package.

The repository currently allows 3D plotting from the ``mayavi`` and ``pyvista`` packages. The ``pyvista`` plots are recommneded, as they are easier to use and modify. However, ``pyvista`` uses ``trame`` as backend, which is slower than ``mayavi``'s native interaction window.

Installation
------------

Both ```mayavi`` and ``pyvista`` packages require the VTK package. To install the latest version of vtk, download the `latest wheels <https://pypi.org/project/vtk/#files>`_ from PYPI based on the operating system and Python version. Then install the wheel using pip (for example for arm macOS with python 3.9):

.. code-block:: bash

   pip install vtk-9.2.6-cp39-cp39-macosx_11_0_arm64.whl

Some Python versions do not have wheels for all the operating systems.

To install the mrfmsim-plot package, clone the repository and install using pip::

   pip install .
