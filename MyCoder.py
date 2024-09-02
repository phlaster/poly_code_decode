from CoderInterface import CoderInterface

class MyCoder(CoderInterface):
    def __init__(self):
        self.latin_lower = 'abcdefghijklmnopqrstuvwxyz'
        self.latin_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.cyrillic_lower = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
        self.cyrillic_upper = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

    def run(self, coder_info: str, string_to_process: str) -> str:
        if coder_info == 'code':
            return self._code(string_to_process)
        elif coder_info == 'decode':
            return self._decode(string_to_process)
        else:
            raise ValueError("Invalid coder_info. Use 'code' or 'decode'.")

    def _code(self, string_to_code: str) -> str:
        return self._shift_chars(string_to_code, 1)

    def _decode(self, string_to_decode: str) -> str:
        return self._shift_chars(string_to_decode, -1)

    def _shift_chars(self, string: str, shift: int) -> str:
        result = []
        for char in string:
            if char in self.latin_lower:
                index = (self.latin_lower.index(char) + shift) % 26
                result.append(self.latin_lower[index])
            elif char in self.latin_upper:
                index = (self.latin_upper.index(char) + shift) % 26
                result.append(self.latin_upper[index])
            elif char in self.cyrillic_lower:
                index = (self.cyrillic_lower.index(char) + shift) % 33
                result.append(self.cyrillic_lower[index])
            elif char in self.cyrillic_upper:
                index = (self.cyrillic_upper.index(char) + shift) % 33
                result.append(self.cyrillic_upper[index])
            else:
                result.append(char)
        return ''.join(result)