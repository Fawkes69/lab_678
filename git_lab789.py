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
def write_file(data, file_path):
    with open(file_path, 'w') as file:
        if file_path.endswith('.json'):
            json.dump(data, file, indent=4)
        elif file_path.endswith('.xml'):
            xml_string = xmltodict.unparse(data, pretty=True)
            file.write(xml_string)
        elif file_path.endswith('.yaml') or file_path.endswith('.yml'):
            yaml.dump(data, file, default_flow_style=False)
        else:
            raise ValueError(f"Unsupported file format: {file_path}")
def convert_file(input_path, output_path):
    data = read_file(input_path)
    write_file(data, output_path)
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: program.exe pathFile1.x pathFile2.y")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    try:
        convert_file(input_path, output_path)
        print(f"Successfully converted {input_path} to {output_path}")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)