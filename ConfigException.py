class ConfigException(Exception):
    def __init__(self, *args):
        if len(args) == 2:
            self.line_no = int(args[0])
            self.message = args[1]
        elif len(args) == 1:
            self.line_no = None
            self.message = args[0]
        elif len(args) == 0:
            self.line_no = None
            self.message = None
        else:
            raise ValueError("Invalid number of arguments")

    def __str__(self):
        if self.line_no:
            return f"ConfigException at line {self.line_no}: {self.message}"
        if self.message:
            return f"ConfigException : {self.message}"
        else:
            return "ConfigException"

