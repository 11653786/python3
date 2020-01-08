class User:

    def __init__(self, name):
        self.name = name

    def get(self):
        print(self.name)


class Role:
    def __init__(self, id, name):
        self.id = id
        self.name = name
