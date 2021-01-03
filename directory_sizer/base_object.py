"""Base Object for shared attributes."""
import math


class BaseObject:
    """Base Object class."""

    def __init__(self, path, size_scalor, verbose=False):
        """Initliase the shared attributes."""
        self.path = path
        self.size = 0
        self.verbose = verbose
        self.size_scalor = size_scalor
        self.size_scaling = self._set_scaling(size_scalor)

    def _set_scaling(self, size_scalor):
        scaling = {
            "B": 1,
            "KB": 1024,
            "MB": math.pow(1024, 2),
            "GB": math.pow(1024, 3),
            "TB": math.pow(1024, 4),
        }

        return scaling.get(size_scalor, 1)

    def set_size(self, size):
        """Set the size of the object in Bytes."""
        self.size = size

    def scale_size(self):
        """Scale the size into the provided scalor, and round to 2dp."""
        self.size = round(self.size / self.size_scaling, 2)
