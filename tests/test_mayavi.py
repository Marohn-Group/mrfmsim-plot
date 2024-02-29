from mrfmsim_plot.mayaviplots import mayavi_image_plane, mayavi_save
import numpy as np
from mayavi import mlab
import pytest


@pytest.fixture
def offscreen():
    """Set mayavi tests to offscreen mode."""

    mlab.options.offscreen = True
    yield
    # turn the option back to default
    mlab.options.offscreen = False


class TestMayaviImagePlane:
    """Test plotting using mayavi with the image_plane function."""

    def test_image_data(self, dataset, grid, offscreen):
        """Test mayavi image data."""

        engine = mayavi_image_plane(dataset, grid).get_engine()
        assert np.array_equal(
            engine.current_scene.children[0].scalar_data, dataset
        )

    def test_image_plane_widgets(self, dataset, grid, offscreen):
        """Test image_plane widgets start at the right index."""

        engine = mayavi_image_plane(dataset, grid).get_engine()
        pipeline = engine.current_scene.children[0].children[0].children
        ipw_x, ipw_y, ipw_z = pipeline[0:3]
        assert ipw_x.ipw.plane_orientation == "x_axes"
        assert ipw_x.ipw.slice_index == 5
        assert ipw_y.ipw.plane_orientation == "y_axes"
        assert ipw_y.ipw.slice_index == 10
        assert ipw_z.ipw.plane_orientation == "z_axes"
        assert ipw_z.ipw.slice_index == 10
    
    def test_image_axes(self, dataset, grid, offscreen):
        """Test if the image has the correct extent (or range)."""
        engine = mayavi_image_plane(dataset, grid).get_engine()
        pipeline = engine.current_scene.children[0].children[0].children
        axes = pipeline[4].axes
        assert np.array_equal(axes.ranges, [-45, 55, -40, 60, -15, 5])

    
    def test_image_size(self, dataset, grid, offscreen):
        """Test if the image has the correct size."""
        engine = mayavi_image_plane(dataset, grid, size=(800, 800)).get_engine()
        scene = engine.current_scene
        assert all(scene.scene.get_size() == (800, 800))

def test_mayavi_plot(dataset, grid, tmpdir):
    """Test the mayavi_plot decorator to see if it saved an image.
    
    Here, we only test that it created a file with the correct name.
    And the file has content.
    """

    @mayavi_save
    def plot(dataset, grid):
        return mayavi_image_plane(dataset, grid)

    plot(dataset, grid, filename=str(tmpdir.join("test.png")))
    assert tmpdir.join("test.png").check()
    assert tmpdir.join("test.png").size() > 0
