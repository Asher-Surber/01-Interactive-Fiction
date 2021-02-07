class Player():
    '''Holds player information such as HP, inventory, and counters.'''
    def __init__(self, hp=15, inventory=[], kill_count=0, lost_item_count=0, story_path=set():
        self.hp = hp
        self.inventory = inventory
        self.kc = kill_count
        self.lic = lost_item_count
        self.story_path = story_path

    def get_item(item):
        inventory = inventory.append(item)
        if type(item) == LostItem:
            lost_item_count += 1
        print("The" + item + "is now in your inventory.")
    
    def use_item(item):
        if item in inventory:
            if type(item) == LostItem:
                return("You can't use this item.")
            if type(item) == HealthItem and hp < 15:
                hp += item.heal_points
                inventory = inventory.remove(item)
                print("You used the " + item + ". Your HP has been restored to " + hp + ".")
    
    def view_inventory():
        return inventory
    
    def kill():
        kill_count += 1
    

    player = Player()