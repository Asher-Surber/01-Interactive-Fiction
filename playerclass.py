class Player():
    '''Holds player information such as HP, inventory, and counters.'''
    def __init__(self, hp=15, inventory=[], kill_count, lost_item_count, story_path):
        self.hp = hp
        self.inventory = inventory
        self.kc = kill_count
        self.lic = lost_item_count
        self.story_path = story_path

    def get_item(item):
        inventory = inventory.append(item)
        if type(item) == LostItem:
            lost_item_count += 1
        print("The")