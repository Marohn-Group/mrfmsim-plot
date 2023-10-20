import pytest
import numpy as np
from mrfmsim.component import Grid


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

    grid = Grid(shape=(11, 21, 21), step=[10, 5, 1], origin=[5, 10, -5])
    return grid
