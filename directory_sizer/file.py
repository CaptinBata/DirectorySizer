"""File class for storing file information."""
from base_object import BaseObject


class File(BaseObject):
    """Finds the size of a given file."""

    def __init__(self, path, size_scalor, verbose=False):
        """Initialise attributes."""
        super().__init__(path, size_scalor, verbose=verbose)
