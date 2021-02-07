class LostItem:
    '''Differentiates key items from ordinary items to aid in types of scoring.'''

    def __init__(self, name, description, item_number):
        self.name = name
        self.description = description
        self.item_number = item_number

silverLocket = LostItem("Silver Locket", "The fighter dropped this. Inside are paintings of what seems to be a family.", 1)
    
woolHat = LostItem("Wool Hat", """An old hat made of sheep's wool and dyed blue. Clearly well-worn.
                        It now has twigs and pine needles stuck into it. Perhaps it was a nest?""", 2)