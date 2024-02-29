import pyvista as pv
from mrfmsim_plot.pvplots import pv_imagedata, pv_save, pv_volume
import numpy as np

class TestImageData:
    """Test the pv_imagedata function."""
    
    def test_image_data(self, dataset, grid):
        """Test if the image data has the correct scalar data values."""
        
        image_data = pv_imagedata(dataset, grid)
        assert np.array_equal(image_data["data"], dataset.flatten(order="F"))
        assert np.array_equal(image_data.dimensions, grid.shape)
        assert np.array_equal(image_data.origin, [grid.extents[0][0], grid.extents[1][0], grid.extents[2][0]])
        assert np.array_equal(image_data.spacing, grid.step)
    
    def test_image_data_name(self, dataset, grid):
        """Test if the image data is created with the correct name."""
        
        image_data = pv_imagedata(dataset, grid, name="new_name")
        assert image_data.active_scalars_name == "new_name"


def test_pv_volume(dataset, grid):
    """Test the pv_volume function."""
    
    p = pv_volume(dataset, grid)
    assert p.renderers[0].background_color == "white"
    assert p.renderers[0].axes_enabled

def test_pv_save(tmpdir):
    """Test the py_save decorator."""
    
    @pv_save
    def plot():
        p = pv.Plotter()
        p.add_mesh(pv.Sphere())
        return p
    
    plot(filename=str(tmpdir.join("test.png")))
    assert tmpdir.join("test.png").check()
    assert tmpdir.join("test.png").size() > 0
