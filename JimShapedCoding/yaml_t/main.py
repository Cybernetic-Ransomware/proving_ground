import yaml
import pprint as pp

with open('config.yaml', 'r') as config:
    parse_yaml = yaml.safe_load(config)

pp.pprint(parse_yaml)
print(parse_yaml['person']['places'][1]['localisation'])
