import json


class VarStorage:
    def __init__(self):
        self.variables = dict()

    def get(self, key):
        if key not in self.variables:
            return None

        return self.variables[key]

    def set(self, key, value=None):
        if not value:
            value = 0

        self.variables[key] = value

    def __str__(self):
        return json.dumps(self.variables, indent=4)
