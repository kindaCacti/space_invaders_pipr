class FileManager():
    def __init__(self, path):
        self._path = path
    
    def write_to_file(self, content):
        file = open(self._path, "w")
        file.write(content)
        file.close()
    
    def read_file(self):
        file = open(self._path, "r")
        content = file.readlines()
        file.close()
        return content[0]