from FileReaderInterface import FileReaderInterface
from contextlib import contextmanager

class MyFileReader(FileReaderInterface):
    @contextmanager
    def read_file(self, file_name: str, buffer_size: int):
        file = None
        try:
            file = open(file_name, 'r')
            yield file
        except IOError as e:
            print(f"Error reading file: {e}")
        finally:
            if file:
                file.close()