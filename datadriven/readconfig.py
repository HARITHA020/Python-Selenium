import os
from configparser import ConfigParser

def get_config(category, key):
    config = ConfigParser()

    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, "..", "config.ini")

    config.read(file_path, encoding="utf-8")

    return config.get(category, key)