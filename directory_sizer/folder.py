"""File class for storing file information."""
from pathlib import Path

from base_object import BaseObject

from file import File


class Folder(BaseObject):
    """Scans and calculates size of a given folder."""

    def __init__(self, path, size_scalor, verbose=False):
        """Intialise attributes."""
        super().__init__(path, size_scalor, verbose=verbose)
        self.folders = []
        self.files = []

    def start(self):
        """Start the directory sizer."""
        print("Scanning provided directory")
        self._scan()
        print("Calculating size of directory")
        self._calculate_size()
        print("Outputting findings into text file in passed directory")
        self._output()

    def verbose_print(self, message, data, scalor=""):
        """Print out the given arguments. Used when verbose is set to true."""
        print(f" - {message}: {data} {scalor}")

    def _scan(self):
        """Scan the given directory for sub folders/files."""
        self.path_object = Path(self.path)
        for sub_contents in self.path_object.iterdir():
            path_string = str(sub_contents.resolve())

            if sub_contents.is_dir():
                if self.verbose:
                    self.verbose_print("Folder found", path_string)
                self.folders.append(
                    Folder(path_string, self.size_scalor, verbose=self.verbose)
                )
                self.folders[-1]._scan()

            if sub_contents.is_file():
                if self.verbose:
                    self.verbose_print("File found", path_string)
                self.files.append(
                    File(path_string, self.size_scalor, verbose=self.verbose)
                )

    def _calculate_file_size(self, files):
        size = 0
        for file in files:
            path_object = Path(file.path)
            stat = path_object.stat()
            file.set_size(stat.st_size)
            size += file.size
            file.scale_size()

            if self.verbose:
                self.verbose_print(
                    f"Size of {file.path}", file.size, scalor=self.size_scalor
                )
        return size

    def _calculate_size(self):
        """Calculate the size of the sub folders/files."""
        size = 0
        for folder in self.folders:
            sub_size = 0
            for sub_folder in folder.folders:
                sub_size += sub_folder._calculate_size()

            sub_size += self._calculate_file_size(folder.files)

            size += sub_size
            folder.set_size(sub_size)
            folder.scale_size()
            if self.verbose:
                self.verbose_print(
                    f"Size of {folder.path}",
                    folder.size,
                    scalor=self.size_scalor,
                )

        size += self._calculate_file_size(self.files)

        self.set_size(size)
        self.scale_size()
        if self.verbose:
            self.verbose_print(
                f"Size of {self.path}", self.size, scalor=self.size_scalor
            )

        return size

    def _output(self):
        """Output the findings of the directory."""
        pass
