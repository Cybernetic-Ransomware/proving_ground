import yaml


data = {
    'name': 'Anthony',
    'age': 32,
    'occupation': 'plumber',
    'languages': {1: 'polish', 2: 'dutch', 3: 'kaszebe'}
}

with open('example_file.yaml', 'w') as f:
    yaml.dump(data, f, default_flow_style=False)
