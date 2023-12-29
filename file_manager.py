class FileManager():
    """
    Class FileManager used to manage files.

    Attributes:
    -----------
    path: str
        string representing a path to a file

    Methods:
    --------
    write_to_file(content: str)
        method writing content to file
    read_file()
        method reading frome file
    """
    def __init__(self, path: str):
        self._path = path

    def write_to_file(self, content: str):
        """writes content to file"""
        file = open(self._path, "w")
        file.write(content)
        file.close()

    def read_file(self) -> str:
        """reads data form file"""
        try:
            file = open(self._path, "r")
            content = file.readlines()
            file.close()
            return content[0]
        except FileNotFoundError:
            self.write_to_file("0")
            return self.read_file()
