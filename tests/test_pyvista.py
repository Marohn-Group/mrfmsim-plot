import pyvista as pv
from mrfmsim_plot.pvplots import create_imagedata, mesh_clip_plane
import numpy as np

pv.OFF_SCREEN = True

def test_create_imagedata(dataset, grid):
    """Test if the image data is created correctly.
    
    Check the grid axes to make sure they are generated correctly.
    """
    image_data = create_imagedata(dataset, grid)

    assert np.array_equal(image_data.dimensions, grid.shape)
    # assert np.array_equal(image_data.origin, grid.grid_origin)
    assert np.array_equal(image_data.spacing, grid.step)
    assert np.array_equal(image_data.point_data["values"], dataset.flatten(order="F"))

    full_grid_array = np.broadcast_arrays(*grid.grid_array)
    assert np.array_equal(image_data.x, full_grid_array[0].flatten(order="F"))
    assert np.array_equal(image_data.y, full_grid_array[1].flatten(order="F"))
    assert np.array_equal(image_data.z, full_grid_array[2].flatten(order="F"))
