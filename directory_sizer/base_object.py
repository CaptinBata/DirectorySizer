"""Base Object for shared attributes."""


class BaseObject:
    """Base Object class."""

    def __init__(self, path, verbose=False):
        """Initliase the shared attributes."""
        self.path = path
        self.size = 0
        self.verbose = verbose
