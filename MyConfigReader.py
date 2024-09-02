import logging
from ConfigReaderInterface import ConfigReaderInterface
from ConfigException import ConfigException

logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

class MyConfigReader(ConfigReaderInterface):
    def read_config(self, config_file_name: str) -> dict:
        try:
            with open(config_file_name, 'r') as config_file:
                for (line_no, line) in enumerate(config_file):
                    if line.strip().startswith('#'):
                        continue
                    splitted = line.strip().split(self._param_delimiter)
                    if len(splitted) != 2:
                        raise ConfigException(line_no, f"Can't parse the line (incorrect format)")
                    key, value = splitted
                    key = key.strip()
                    value = value.strip()
                    
                    if key not in self._config_dict:
                        raise ConfigException(line_no, f"Unknown parameter: {key}")
                    
                    if key == self.buffer_size_param_name:
                        try:
                            self._config_dict[key] = int(value)
                            if self._config_dict[key] <= 0:
                                raise ValueError
                        except ValueError:
                            raise ConfigException(line_no, f"Buffer size must be a positive integer: {value}")
                    elif key == self.coder_run_option_param_name:
                        if value not in ["code", "decode"]:
                            raise ConfigException(line_no, f"Invalid coder option: {value}")
                        self._config_dict[key] = value
                    else:
                        self._config_dict[key] = value
            for key, value in self._config_dict.items():
                if value is None:
                    raise ConfigException(f"Missing parameter: {key}")

            return self._config_dict

        except IOError as e:
            logging.error(f"Error reading config file: {e}")
            raise ConfigException(f"Error reading config file: {e}")
        except Exception as e:
            logging.error(f"Error in config file: {e}")
            raise ConfigException(f"Error in config file: {e}")