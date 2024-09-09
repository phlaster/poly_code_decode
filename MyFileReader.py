from FileReaderInterface import FileReaderInterface
from contextlib import contextmanager

class MyFileReader(FileReaderInterface):
    
    @contextmanager
    def read_file(self, file_name: str, buffer_size: int):
        try:
            with open(file_name, 'r') as file:
                yield iter(lambda: file.read(buffer_size), '')
        except IOError as e:
            print(f"Error while reading file: {e}")
        except Exception as e:
            print(f"An error occurred while reading the file: {e}")
