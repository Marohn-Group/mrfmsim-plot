from mrfmsim_plot.pvplot import pv_imagedata, pv_plot_preset, pv_preset_volume
import numpy as np


class TestImageData:
    """Test the pv_imagedata function."""

    def test_image_data(self, dataset, grid):
        """Test if the image data has the correct scalar data values."""

        image_data = pv_imagedata(dataset, grid)
        assert np.array_equal(image_data["data"], dataset.flatten(order="F"))
        assert np.array_equal(image_data.dimensions, grid.grid_shape)
        assert np.array_equal(
            image_data.origin,
            [grid.grid_extents[0][0], grid.grid_extents[1][0], grid.grid_extents[2][0]],
        )
        assert np.array_equal(image_data.spacing, grid.grid_step)

    def test_image_data_name(self, dataset, grid):
        """Test if the image data is created with the correct name."""

        image_data = pv_imagedata(dataset, grid, name="new_name")
        assert image_data.active_scalars_name == "new_name"


def test_pv_preset_volume(dataset, grid):
    """Test if pv_preset_volume returns the correct preset dictionary."""

    preset = pv_preset_volume(dataset, grid)

    # Check if the preset contains all expected keys
    expected_keys = ["add_volume", "window_size", "add_scalar_bar", "add_axes"]
    for key in expected_keys:
        assert key in preset

    # Check volume settings
    assert preset["add_volume"]["volume"].active_scalars_name == "data"
    assert preset["add_volume"]["clim"] == [dataset.min(), dataset.max()]
    assert preset["add_volume"]["cmap"] == "viridis"
    assert preset["add_volume"]["opacity"] == 0.8
    assert preset["add_volume"]["show_scalar_bar"] == False

    # Test with custom parameters
    custom_preset = pv_preset_volume(
        dataset,
        grid,
        name="custom_data",
        add_volume={"cmap": "plasma", "opacity": 0.5},
        window_size=[800, 600],
    )

    assert custom_preset["add_volume"]["cmap"] == "plasma"
    assert custom_preset["add_volume"]["opacity"] == 0.5
    assert custom_preset["window_size"] == [800, 600]
    assert custom_preset["add_volume"]["volume"].active_scalars_name == "custom_data"


def test_pv_plot_preset(dataset, grid):
    """Test if pv_plot_preset correctly applies preset parameters."""

    # Create a simple preset dictionary
    preset = {
        "window_size": [400, 300],
        "add_axes": {},
        "add_text": {"text": "Test", "position": "upper_left"},
    }

    # Create plotter with preset
    plotter = pv_plot_preset(preset)

    # Check if the preset parameters were applied
    assert plotter.window_size == [400, 300]

    # Test with more complex parameters
    complex_preset = {
        "window_size": [800, 600],
        "add_axes": {"xlabel": "X", "ylabel": "Y", "zlabel": "Z"},
        "background_color": "white",
    }

    complex_plotter = pv_plot_preset(complex_preset)
    assert complex_plotter.window_size == [800, 600]
    assert complex_plotter.background_color == "white"

    # Test method calls with dictionaries
    image_data = pv_imagedata(dataset, grid, name="data")
    preset = {
        "add_volume": {"volume": image_data, "opacity": 0.7},
        "add_scalar_bar": {"title": "Test Bar", "n_labels": 3},
    }

    # This should call the methods without errors
    plotter = pv_plot_preset(preset)
    scalar_bar_actor = plotter.scalar_bars["Test Bar"]
    # Test number of labels - VTK uses GetNumberOfLabels() method
    assert scalar_bar_actor.GetNumberOfLabels() == 3
    assert scalar_bar_actor.GetTitle() == "Test Bar"
