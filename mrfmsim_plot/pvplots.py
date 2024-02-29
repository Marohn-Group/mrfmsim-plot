import pyvista as pv


def pv_imagedata(dataset, grid, name="data"):
    """Create a PyVista ImageData object from a numpy array and its grid.

    The origin of the PyVista object is not the same as the grid origin.
    In mrfmsim, the grid origin is defined as the middle of the grid.
    In pyvista plots, the origin is defined as the lower left corner
    (southwest corner) of the grid.
    """

    image_data = pv.ImageData()
    image_data.dimensions = grid.shape
    image_data.origin = [grid.extents[0][0], grid.extents[1][0], grid.extents[2][0]]
    image_data.spacing = grid.step

    # pyvsita sets the grid up as the F order, different from the mgrid
    # default generation
    image_data[name] = dataset.flatten(order="F")

    return image_data


def pv_volume(dataset, grid, name="data", background_color="white", **kwargs):
    """Create a PyVista volume plot object.
    
    :param np.array dataset: the dataset to plot
    :param np.array grid: the grid of the dataset
    :param str name: the name of the dataset
    :param str background_color: the background color of the plot
    :param kwargs: additional keyword arguments to pass to the add_volume method
    """
    image_data = pv_imagedata(dataset, grid, name)
    p = pv.Plotter()
    p.add_volume(image_data, **kwargs)
    p.background_color = background_color
    p.add_axes()
    return p



def pv_save(func):
    """Decorator to save the plot to a file directly.
    
    A decorator is used because the offscreen option needs to be set before the
    pyvista object is created. The decorator adds a keyword filename argument
    to the plotting function.
    """

    def wrapper(*args, filename, **kwargs):
        pv.OFF_SCREEN = True
        p = func(*args, **kwargs)
        p.screenshot(filename)
        p.close()
        pv.OFF_SCREEN = False

    return wrapper
