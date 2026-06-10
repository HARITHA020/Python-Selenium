from configparser import ConfigParser
import os

def get_config(category, key):
    config = ConfigParser()

    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, "config.ini")

    print("LOADING:", file_path)

    with open(file_path, "r", encoding="utf-8-sig") as f:
        config.read_file(f)

    print("SECTIONS:", config.sections())

    return config.get(category, key)