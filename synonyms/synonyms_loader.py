import yaml

class synonyms_loader():
    def __init__(self):
        with open(".data/synonyms.yaml", 'r') as stream:
            try:
                print(yaml.safe_load(stream))
            except yaml.YAMLError as exc:
                print(exc)