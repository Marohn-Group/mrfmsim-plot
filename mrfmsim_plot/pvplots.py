import pyvista as pv


def create_imagedata(dataset, grid):
    """Create a pyvista ImageData object from a numpy array and its grid.

    The origin of the pyvista object is not the same as the grid origin.
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
    image_data.point_data["values"] = dataset.flatten(order="F")

    return image_data


def mesh(dataset, grid, off_screen=False, **kwargs):
    """Create mesh plot from pyvista.

    The function takes the numpy array and the grid information.
    The function converts the numpy array into a vtk object, and
    uses the grid array to scale the plot axis.
    """
    image_data = create_imagedata(dataset, grid)

    p = pv.Plotter(off_screen=off_screen)
    p.add_mesh(image_data, **kwargs)

    return p


def mesh_clip_plane(dataset, grid, off_screen=False, **kwargs):
    """Create mesh clip plane plot from pyvista.

    The function takes the numpy array and the grid information.
    The function converts the numpy array into a vtk object, and
    uses the grid array to scale the plot axis.
    """
    image_data = create_imagedata(dataset, grid)

    p = pv.Plotter(off_screen=off_screen)
    p.add_mesh_clip_plane(image_data, **kwargs)

    return p


def volume(dataset, grid, off_screen=False, **kwargs):
    """Create a volume plot from pyvista.

    The function takes the numpy array and the grid information.
    The function converts the numpy array into a vtk object, and
    uses the grid array to scale the plot axis.
    """
    image_data = create_imagedata(dataset, grid)

    p = pv.Plotter(off_screen=off_screen)
    p.add_volume(image_data, **kwargs)

    return p


def volume_clip_plane(dataset, grid, off_screen=False, **kwargs):
    """Create a volume clip plane plot from pyvista."""
    image_data = create_imagedata(dataset, grid)

    p = pv.Plotter(off_screen=off_screen)
    p.add_volume_clip_plane(image_data, **kwargs)

    return p
