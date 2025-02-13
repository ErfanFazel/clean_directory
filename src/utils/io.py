import json 


def read_json(file_path):
    """
    Read a json file from the given file path
    """
    with open(file_path) as f:
        return json.load(f)