import yaml

from utils.env import Env


class ConfigReader:
    PATH_YAML = 'config/config.yml'

    def __init__(self, config_path=PATH_YAML, env=Env.DEV.value):
        self.config_path = config_path
        with open(self.config_path, 'r', encoding='utf-8') as f:
            all_config = yaml.safe_load(f)
            self.config = all_config.get(env, {})

    def get(self, key, default=None):
        return self.config.get(key, default)