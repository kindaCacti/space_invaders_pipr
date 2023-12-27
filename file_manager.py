class FileManager():
    def __init__(self, path: str):
        self._path = path

    def write_to_file(self, content: str):
        file = open(self._path, "w")
        file.write(content)
        file.close()

    def read_file(self):
        try:
            file = open(self._path, "r")
            content = file.readlines()
            file.close()
            return content[0]
        except FileNotFoundError:
            self.write_to_file("0")
            return self.read_file()
