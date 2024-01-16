#!/usr/bin/env python3

import logging
import sys

from CwrdCoder import CwrdCoder
from ConfigException import ConfigException
from MyConfigReader import MyConfigReader
from MyFileReader import MyFileReader


class MainClass:
    def __init__(self):
        self._config_reader: ConfigReader = None
        self._file_reader: FileReader = None
        self._coder: Coder = None

    def run(self, config_file_name: str) -> str:
        result = ""
        try:
            configuration = self._config_reader.read_config(config_file_name)
            file_name = configuration[self._config_reader.file_name_for_coder_param_name]
            buffer_size = configuration[self._config_reader.buffer_size_param_name]
            coder_configuration = configuration[self._config_reader.coder_run_option_param_name]

            with self._file_reader.read_file(file_name, buffer_size) as chunks:
                for chunk in chunks:
                    chunk_res = self._coder.run(coder_configuration, chunk)
                    result += chunk_res
                return result
        except ConfigException as e:
            logging.error(e)
            return ""


if __name__ == '__main__':
    argv_config_file_name = input()
    main_class = MainClass()
    print(main_class.run(argv_config_file_name))
