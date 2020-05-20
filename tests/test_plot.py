import numpy as np
import pytest

from inorixcv import plot


def test_multi_imshow():
    images = [np.random.rand(128, 128, 3) for _ in range(2)]
    with pytest.raises(ValueError):
        plot.multi_imshow(images, titles=["a", "b", "c", "d"])
