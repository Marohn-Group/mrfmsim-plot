from mrfmsim_plot.mplots import image_plane
import numpy as np

class TestMayaviImagePlane:
    """Test plotting using mayavi with the image_plane function."""

    def test_image_data(self, dataset, grid):
        """Test mayavi image data."""

        engine = image_plane(dataset, grid).get_engine()
        assert np.array_equal(
            engine.current_scene.children[0].scalar_data, dataset
        )

    def test_image_plane_widgets(self, dataset, grid):
        """Test image_plane widgets start at the right index."""

        engine = image_plane(dataset, grid).get_engine()
        pipeline = engine.current_scene.children[0].children[0].children
        ipw_x, ipw_y, ipw_z = pipeline[0:3]
        assert ipw_x.ipw.plane_orientation == "x_axes"
        assert ipw_x.ipw.slice_index == 5
        assert ipw_y.ipw.plane_orientation == "y_axes"
        assert ipw_y.ipw.slice_index == 10
        assert ipw_z.ipw.plane_orientation == "z_axes"
        assert ipw_z.ipw.slice_index == 10
    
    def test_image_axes(self, dataset, grid):
        """Test if the image has the correct extent (or range)."""
        engine = image_plane(dataset, grid).get_engine()
        pipeline = engine.current_scene.children[0].children[0].children
        axes = pipeline[4].axes
        assert np.array_equal(axes.ranges, [-45, 55, -40, 60, -15, 5])
