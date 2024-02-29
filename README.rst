mrfmsim-plot
=============

This module provides scripts for generating plots for magnetic resonance force microscopy 
experiments. It serves as a plugin library for the 
`mrfmsim repository <https://github.com/Marohn-Group/mrfmsim>`_ package.

The repository currently allows 3D plotting from the ``mayavi`` and ``pyvista`` packages. 
The ``pyvista`` plots are recommended, as they are easier to use and modify. However, ``pyvista`` 
uses ``trame`` as the backend, which is slower than ``mayavi``'s native interaction window.

Installation
------------

Both ```mayavi`` and ``pyvista`` packages require the VTK package. To install the latest version of 
vtk, download the `latest wheels <https://pypi.org/project/vtk/#files>`_ from PYPI based on the 
operating system and Python version. Then install the wheel using pip (for example, for arm macOS 
with python 3.10), download the file "vtk-9.3.0-cp311-cp311-macosx_11_0_arm64.whl" and install
the file using pip:

.. code-block:: bash

   pip install vtk-9.3.0-cp311-cp311-macosx_11_0_arm64.whl

Note the Python requirement for this package is 3.10 and the vtk versions tested are
9.2.6 and 9.3.0.

To install the mrfmsim-plot package, clone the repository and install using pip::

   pip install .

Usage
-----

The *mrfmsim-plot* does not provide a unified interface for the Mayavi and PyVista packages due
to their different vtk implementations. Currently, this package provides two pre-build plotting
method --- Mayavi scalar field with sliding plane widget and PyVista volume plots. In addition,
we provide a simple conversion function for `mrfmsim.Grid` object to `pyvista.ImageData` object.
Both package provide the decorator `mayavi_save` and `pyvista_save` for offscreen rendering and
save the images to files. Users are encouraged to explore the codebase and create their own plotting
functions with the two packages.

The entry point for the package is designed to include all functions in the "mayaviplots" and
"pyvistaplots" modules. The functions are named with `mayavi_` and `pv_` prefixes to indicate the
origin of the function. 

.. code-block:: python

   from mrfmsim.plot import mayavi_image_plane, pv_volume


Mayavi
~~~~~~~~~~~~~~~~~~~

Given a `mrfmsim.Grid` object `grid` and data array `dataset` with the same dimensions,
to plot the scalar plot with three sliding plane widgets

.. code-block:: python

   from mrfmsim.plot import mayavi_image_plane

   p = mayavi_scalar_field(grid, dataset)
   p.show()

Use the `mayavi_save` decorator to wrap the plot function to save the image to file
the decorator adds a filename keyword argument to the function. The decorator can
be used with `@` syntax sugar to decorate a new function definition.

.. code-block:: python

   from mrfmsim.plot import mayavi_save

   mayavi_image_plane_save = mayavi_save(mayavi_image_plane)
   mayavi_image_plane_save(grid, dataset, filename=filename)


PyVista
~~~~~~~~~~~~~~~~~~~~

Given a `mrfmsim.Grid` object `grid` and data array `dataset` with the same dimensions,
to plot the volume plot

.. code-block:: python

   from mrfmsim.plot import pv_volume

   p = pv_volume(grid, dataset, name='new_data')
   p.show()

Use the `pv_save` decorator to wrap the plot function to save the image to file
the decorator adds a filename keyword argument to the function. The decorator can
be used with `@` syntax sugar to decorate a new function definition.

.. code-block:: python

   from mrfmsim.plot import pv_save

   pv_volume_save = pyvista_save(pv_volume)
   pv_volume_save(grid, dataset, name='new_data', filename=filename)

In addition, we provide the function that convert the `mrfmsim.Grid` object to `pyvista.ImageData`

.. code-block:: python

   from mrfmsim.plot import pv_imagedata

   image_data = pv_imagedata(dataset, grid)
