import pyvista as pv
from mrfmsim_plot.pvplot import pv_imagedata, pv_plot_preset, VolumePreset_tab20b
import numpy as np


class TestImageData:
    """Test the pv_imagedata function."""

    def test_image_data(self, dataset, grid):
        """Test if the image data has the correct scalar data values."""

        image_data = pv_imagedata(dataset, grid)
        assert np.array_equal(image_data["data"], dataset.flatten(order="F"))
        assert np.array_equal(image_data.dimensions, grid.shape)
        assert np.array_equal(
            image_data.origin,
            [grid.extents[0][0], grid.extents[1][0], grid.extents[2][0]],
        )
        assert np.array_equal(image_data.spacing, grid.step)

    def test_image_data_name(self, dataset, grid):
        """Test if the image data is created with the correct name."""

        image_data = pv_imagedata(dataset, grid, name="new_name")
        assert image_data.active_scalars_name == "new_name"


def test_pv_plot_preset(dataset, grid):
    """Test the pv_volume function."""

    preset = VolumePreset_tab20b(dataset, grid)
    p = pv_plot_preset(preset)

    assert p.renderers[0].background_color == "whitesmoke"
    assert p.renderers[0].axes_enabled

def test_pv_preset_changes(dataset, grid):
    """Test if the preset changes the plot correctly."""

    preset = VolumePreset_tab20b(dataset, grid)
    del preset['add_axes']
    p = pv_plot_preset(preset)

    assert not p.renderers[0].axes_enabled
