import yaml
import pprint as pp


with open('settings.yml', 'r') as f:
    parse_yaml = yaml.safe_load(f)

pp.pprint(f"{parse_yaml['person']['weight']:.2f} in kilograms ")

# source: https://youtu.be/S6-7NaKFqSs
