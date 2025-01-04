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

Both ``mayavi`` and ``pyvista`` packages require the VTK package.
The VTK package can be installed with pip and it is included in pyvista.
The package should work with ``pyvista`` by default::

   pip install .

The ``mayavi`` package, however, is very difficult to work with due to
build and dependency issues. Therefore the installation is optional. To install
mayavi packages::

   pip install .[mayavi]

It is recommended to manually install the dependency for mayavi. To do that first
install the vtk package (version 9.3.1) using pip::

   pip install vtk==9.3.1

Then install the mayavi package (with a fresh build)::

   pip install mayavi==4.8.2 --no-cache-dir --verbose  --no-build-isolation

Lastly install the pyqt5 package::

   pip install pyqt5==5.15.11

Usage
-----

The *mrfmsim-plot* provides some basic interaction with the Mayavi and PyVista packages.
The behaviors of the two modules are different because of very different ploting implementations.

For the Mayavi package, a pre-defined 3D plotting function ``mayavi_image_plane`` is provided.
To plot a dataset, the original ``mrfmsim.Grid`` object and the data array are required.

.. code-block:: python

   from mrfmsim.plot import mayavi_image_plane

   mplot = mayavi_image_plane(dataset, grid)
   mplot.show()

To save the image without rendering the window,

.. code-block:: python

   from mayavi import mlab
   from mrfmsim.plot import mayavi_image_plane

   mlab.options.offscreen = True
   mplot = mayavi_image_plane(dataset, grid)
   mplot.savefig(filename)
   mplot.close()
   ## turn the screen back on
   # mlab.options.offscreen = False

For the PyVista package, because the plotting and the additional settings are additive, we
provide style presets and a function ``pv_plot_present`` that can plot the preset.
For the detailed preset settings, please refer to the "pvplot.py" file.

.. code-block:: python

   from mrfmsim.pvplot import pv_plot_present, VolumePreset_tab20b

   present = VolumePreset_tab20b(dataset, grid)
   pl = pv_plot_present(present)
   pl.show()

The preset is a dictionary class. Changes can be made to the preset dictionary
directly or add keyward arguments during the present initialization.

.. code-block:: python

   from mrfmsim.pvplot import pv_plot_present, VolumePreset_tab20b

   present = VolumePreset_tab20b(dataset, grid, window_size=(800, 800))
   del present['add_axes'] # remove the axes
   pl = pv_plot_present(present)
   pl.show()

Similar, to save the plot, we need to turn off the interactive window.

.. code-block:: python

   from mrfmsim.pvplot import pv_plot_present, VolumePreset_tab20b
   import pyvista as pv
   
   pv.OFF_SCREEN = True
   present = VolumePreset_tab20b(dataset, grid)
   pl = pv_plot_present(present)
   
   # ``.screenshot`` method can also be used, check the pyvista documentation
   # for more details.
   pl.save_graphic(filename, ...)

   # turn the screen back on
   # pv.OFF_SCREEN = False
