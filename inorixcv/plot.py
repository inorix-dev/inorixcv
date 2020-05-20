import math
from typing import List, Tuple, Union

import matplotlib.pyplot as plt
import numpy as np


def multi_imshow(
    images: List[np.ndarray],
    titles: List[str] = None,
    num_columns: int = -1,
    figsize: Union[str, Tuple[float, float]] = "auto",
):
    """Plot multiple images.

    Args:
        images (List[np.ndarray]): List of image
        titles (List[str], optional): List of title. Defaults to None.
        num_columns (int, optional): Number of columns. -1 is an alias to len(images). Defaults to -1.
        figsize (Union[str, Tuple[float, float]], optional): Plot size (width, height). If "auto" is given, plot size is
            set to the appropriate size automatically. Defaults to "auto".
    """
    if titles is not None and len(images) != len(titles):
        raise ValueError

    if num_columns == -1:
        num_columns = len(images)
    num_rows = math.ceil(len(images) / num_columns)

    if figsize == "auto":
        figsize = (num_columns * 3, num_rows * 3)
    plt.figure(figsize=figsize)

    for i, image in enumerate(images):
        plt.subplot(num_rows, num_columns, i + 1)
        plt.imshow(image)
        if titles is not None:
            plt.title(titles[i])
        plt.axis("off")

    plt.tight_layout()
    plt.show()
