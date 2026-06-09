from configparser import ConfigParser
import os

def get_config(category, key):
    config = ConfigParser()

    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, "..", "config.ini")

    print("LOADING CONFIG FROM:", file_path)

    read_files = config.read(file_path, encoding="utf-8")

    print("CONFIG READ RESULT:", read_files)
    print("AVAILABLE SECTIONS:", config.sections())

    return config.get(category, key)