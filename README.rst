mrfmsim-plot
=============

This module provides presets for generating plots for magnetic resonance force microscopy 
experiments. 

The repository currently allows 3D plotting from the `Mayavi <https://docs.enthought.com/mayavi/mayavi/>`_
and `PyVista <https://docs.pyvista.org/>`_ packages. 
The PyVista plots are recommended, as they are easier to use and modify. However, PyVista
uses ``trame`` as the backend, which is slower than Mayavi's native interaction window.

Installation
------------

Both Mayavi and PyVista packages require the VTK package.
The VTK package can be installed with pip, and it is included in PyVista.
The package should work with PyVista by default::

   pip install .

The Mayavi package, however, is very difficult to work with due to
build and dependency issues. Therefore the installation is optional. To install
mayavi packages::

   pip install .[mayavi]

It is recommended to manually install the dependency for Mayavi. To do that first
install the vtk package (version 9.3.1) using pip::

   pip install vtk==9.3.1

Then install the Mayavi package (with a fresh build, and currently only supports
up to numpy 1.26.4)::

   pip install mayavi==4.8.2 --no-cache-dir --verbose  --no-build-isolation

Lastly install the pyqt5 package::

   pip install pyqt5==5.15.11

Usage
-----

The *mrfmsim-plot* provides some basic interaction with the Mayavi and PyVista packages.
The behaviors of the two modules are different because of very different plotting implementations.

For the Mayavi package, a pre-defined 3D plotting function ``mayavi_image_plane`` is provided.
To plot a dataset, the original ``mrfmsim.component.Grid`` object and the data array are required.

Here, we create an example dataset and a grid object.

.. code-block:: python

   from mrfmsim.component import Grid
   import numpy as np

   grid = Grid(grid_shape=(3, 3, 3), grid_step=[1, 1, 1], grid_origin=[0, 0, 0])
   dataset = np.random.rand(*grid.grid_shape)

.. code-block:: python

   from mrfmsim_plot.mayaviplot import mayavi_image_plane

   mplot = mayavi_image_plane(dataset, grid)
   mplot.show()

To save the image without rendering the window,

.. code-block:: python

   from mayavi import mlab
   from mrfmsim_plot.mayaviplot import mayavi_image_plane

   mlab.options.offscreen = True
   mplot = mayavi_image_plane(dataset, grid)
   mplot.savefig(filename)
   mplot.close()
   ## turn the screen back on
   # mlab.options.offscreen = False

For the PyVista package, because the plotting and the additional settings are additive, we
provide style presets and a function ``pv_plot_preset`` that can plot the preset.
See `pyvista.Plotter.add_volume <https://docs.pyvista.org/api/plotting
/_autosummary/pyvista.plotter.add_volume>`_
for more plotting options.

.. code-block:: python

   from mrfmsim_plot.pvplot import pv_plot_preset, pv_preset_volume

   present = pv_preset_volume(dataset, grid)
   pl = pv_plot_preset(present)
   pl.show()

The preset is a dictionary class with some parameter presets. Changes can
be made by adding parameters to the ``pv_preset_volume`` function. Any
modification will update the preset dictionary, including the nested ones.

.. code-block:: python

   from mrfmsim_plot.pvplot import pv_plot_preset, pv_preset_volume

   present = pv_preset_volume(dataset, grid, window_size=(800, 800))
   pl = pv_plot_preset(present)
   pl.show()

Similarly, to save the plot, we need to turn off the interactive window.

.. code-block:: python

   from mrfmsim_plot.pvplot import pv_plot_preset, pv_preset_volume

   present = pv_preset_volume(dataset, grid, window_size=(800, 800))
   pl = pv_plot_preset(present)
   pl.screenshot(filename)
   pl.close()
