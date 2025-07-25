import yaml

class ConfigParser:

    _instance = None

    def __new__(cls, *args, **kwargs) -> "ConfigParser":
        if not cls._instance:
            cls._instance = super(ConfigParser, cls).__new__(cls)
            cls._instance.config_file = "./config/config.yaml"
            cls._instance.config = cls._instance.load_config()
        return cls._instance

    def load_config(self) -> dict:
        with open(self.config_file, "r") as file:
            config = yaml.safe_load(file)
            self.config = config
        return config

    def get_config(self) -> dict:
        return self.config
