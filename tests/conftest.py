import pytest
import numpy as np


@pytest.fixture
def dataset():
    """Setup a random dataset."""
    return np.random.rand(11, 21, 21)


@pytest.fixture
def grid():
    """Setup a grid array of shape (11, 21, 21).

    The grid has the origin of 5, 10, -5; and the extent
    is [-45, 55, -40, 60, -15, 5].
    """

    class Grid:
        """A mock mrfmsim grid."""

        def __init__(self, grid_shape, grid_step, grid_origin):
            self.grid_shape = grid_shape
            self.grid_step = grid_step
            self.grid_origin = grid_origin

            # Calculate grid extents based on shape, step, and origin
            self.grid_extents = []
            for i in range(3):
                start = (
                    self.grid_origin[i]
                    - self.grid_step[i] * (self.grid_shape[i] - 1) * 0.5
                )
                end = (
                    self.grid_origin[i]
                    + self.grid_step[i] * (self.grid_shape[i] - 1) * 0.5
                )
                self.grid_extents.append([start, end])
            self.grid_extents = np.array(self.grid_extents)
            # Create open grid directly with np.ogrid
            self.grid_array = np.ogrid[
                self.grid_extents[0][0] : self.grid_extents[0][1] : self.grid_shape[0]
                * 1j,
                self.grid_extents[1][0] : self.grid_extents[1][1] : self.grid_shape[1]
                * 1j,
                self.grid_extents[2][0] : self.grid_extents[2][1] : self.grid_shape[2]
                * 1j,
            ]

    grid = Grid(grid_shape=(11, 21, 21), grid_step=[10, 5, 1], grid_origin=[5, 10, -5])
    return grid
