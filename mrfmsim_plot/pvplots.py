import pyvista as pv


def create_imagedata(dataset, grid):
    """Create a pyvista ImageData object from a numpy array and its grid.

    The origin of the pyvista object is not the same as the grid origin.
    In mrfmsim, the grid origin is defined as the middle of the grid.
    In pyvista plots, the origin is defined as the lower left corner
    (southwest corner) of the grid.
    """

    extents = grid.grid_extents(grid.grid_range, grid.grid_origin)

    image_data = pv.ImageData()
    image_data.dimensions = grid.grid_shape
    image_data.origin = [extents[0][0], extents[1][0], extents[2][0]]
    image_data.spacing = grid.grid_step

    # pyvsita sets the grid up as the F order, different from the mgrid
    # default generation
    image_data.point_data["values"] = dataset.flatten(order="F")

    return image_data


def mesh_clip_plane(dataset, grid, *args, **kwargs):
    """Create mesh clip plane plot from pyvista.

    The function takes the numpy array and the grid information.
    The function converts the numpy array into a vtk object, and
    uses the grid array to scale the plot axis.
    """
    image_data = create_imagedata(dataset, grid)

    p = pv.Plotter()
    p.add_mesh_clip_plane(image_data)

    return p


def transparent_volume(
    dataset, grid, opacity, opacity_unit_distance, colormap=None, *args, **kwargs
):
    """Create a transparent volume plot from pyvista.

    The function takes the numpy array and the grid information.
    The function converts the numpy array into a vtk object, and
    uses the grid array to scale the plot axis.
    """
    image_data = create_imagedata(dataset, grid)

    p = pv.Plotter()
    p.add_volume(
        image_data,
        opacity=opacity,
        opacity_unit_distance=opacity_unit_distance,
        cmap=colormap or "jet",
    )

    return p
