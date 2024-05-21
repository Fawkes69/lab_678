pip install json xmltodict pyyaml
python program.py pathFile1.x pathFile2.y
import sys
import json
import yaml
import xmltodict
def read_file(file_path):
    with open(file_path, 'r') as file:
        if file_path.endswith('.json'):
            return json.load(file)
        elif file_path.endswith('.xml'):
            return xmltodict.parse(file.read())
        elif file_path.endswith('.yaml') or file_path.endswith('.yml'):
            return yaml.safe_load(file)
        else:
            raise ValueError(f"Unsupported file format: {file_path}")