from typing import AnyStr, Dict

from yaml import safe_load


class Config(dict):
    def __init__(self, path: AnyStr) -> None:
        self.path = path
        super().__init__()

    def load_config(self):
        with open(self.path, 'r') as config_file:
            config: Dict = safe_load(config_file)
            self.update(config)
        return self
