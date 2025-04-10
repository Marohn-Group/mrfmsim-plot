import pyvista as pv
from collections import UserDict


def pv_imagedata(dataset, grid, name="data"):
    """Create a PyVista ImageData object from a numpy array and its grid.

    The origin of the PyVista object is not the same as the grid origin.
    In mrfmsim, the grid origin is defined as the middle of the grid.
    In pyvista plots, the origin is defined as the lower left corner
    (southwest corner) of the grid.
    """

    image_data = pv.ImageData()
    image_data.dimensions = grid.grid_shape
    image_data.origin = [
        grid.grid_extents[0][0],
        grid.grid_extents[1][0],
        grid.grid_extents[2][0],
    ]
    image_data.spacing = grid.grid_step

    # pyvsita sets the grid up as the F order, different from the mgrid
    # default generation
    image_data[name] = dataset.flatten(order="F")

    return image_data


def pv_plot_preset(preset):
    """Create a PyVista plot object with preset parameters.

    :param np.array dataset: the dataset to plot
    :param np.array grid: the grid of the dataset
    :param str plot_type: the type of plot to create
    :param kwargs: additional keyword arguments to pass to the plot function
    """

    p = pv.Plotter()
    for key, value in preset.items():
        if isinstance(value, dict):
            getattr(p, key)(**value)
        else:
            setattr(p, key, value)
    return p


def pv_preset_volume(dataset, grid, name="data", **kwargs):
    """Create a preset for volume rendering.

    The keyword arguments are dictionary, and the content
    is updated to the present dictionary.
    """

    image_data = pv_imagedata(dataset, grid, name)

    preset_params = {
        "add_volume": {
            "volume": image_data,
            "clim": [dataset.min(), dataset.max()],
            "cmap": "viridis",
            "opacity": 0.8,
            "show_scalar_bar": False,
        },
        "window_size": (512, 768),
        "add_scalar_bar": {
            "title": "Data",
            "vertical": True,
            "position_x": 0.8,
            "position_y": 0.3,
            "fmt": "%.2e",
            "n_labels": 5,
        },
        "add_axes": {},
    }

    for key, value in kwargs.items():
        if key in preset_params and isinstance(preset_params[key], dict):
            preset_params[key].update(value)
        else:
            preset_params[key] = value
    return preset_params
