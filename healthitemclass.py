class HealthItem:
    '''Allows items to have healing properties.'''

    def __init__(self, name, description, heal_points):
        self.name = name
        self.description = description
        self.heal_points = heal_points
    
redBerry = HealthItem("Red Berry", "A round, red berry. Smells sweet, appears to be juicy. Most likely not poisonous.", 1)
