class AnimalList():

    """
    This will create an animal list
    """

    def __init__(self, name, description, color):
        self.name = name
        self.description = description
        self.color = color

    def get_overview(self):
        return f"{self.name} and {self.description}"

    def full_info(self):
        return f"{self.name} and {self.description} and {self.color}"


list = AnimalList('Jaguar', 'It is so fast its very crazy', 'Blue')
print(list.color)
print(list.get_overview())