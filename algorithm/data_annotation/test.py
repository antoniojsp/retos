import json

def parse_json(file_path):
    with open(file_path, 'r') as file:
        try:
            data = json.load(file, object_pairs_hook=OrderedDict)
        except json.JSONDecodeError as e:
            print(f"JSON decode error: {e}")
            exit(1)
    return data

data = parse_json('data.json')