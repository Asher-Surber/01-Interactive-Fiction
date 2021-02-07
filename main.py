#!/usr/bin/env python3
import sys, os, json, re
import playerclass, healthitemclass, lostitemclass
assert sys.version_info >= (3,9), "This script requires at least Python 3.9"

# import os,json
def load(l):
    f = open(os.path.join(sys.path[0], l))
    data = f.read()
    j = json.loads(data)
    return j

# Removes Harlowe formatting from Twison description
def format_passage(description):
    description = re.sub(r'//([^/]*)//',r'\1',description)
    description = re.sub(r"''([^']*)''",r'\1',description)
    description = re.sub(r'~~([^~]*)~~',r'\1',description)
    description = re.sub(r'\*\*([^\*]*)\*\*',r'\1',description)
    description = re.sub(r'\*([^\*]*)\*',r'\1',description)
    description = re.sub(r'\^\^([^\^]*)\^\^',r'\1',description)
    description = re.sub(r'(\[\[[^\|]*?)\|([^\]]*?\]\])',r'\1->\2',description)
    description = re.sub(r'\[\[([^(->\])]*?)->[^\]]*?\]\]',r'[ \1 ]',description)
    description = re.sub(r'\[\[(.+?)\]\]',r'[ \1 ]',description)
    # instead of cleaning up the links in the description text, remove them entirely
    description = re.sub(r'(\[\[[^\|]*?)\|([^\]]*?\]\])',r'\1->\2',description)
    description = re.sub(r'\[\[([^(->\])]*?)->[^\]]*?\]\]',r'[ \1 ]',description)
    description = re.sub(r'\[\[(.+?)\]\]\n*','',description)
    return description

def find_passage(game_desc, pid):
    for p in game_desc["passages"]:
        if p["pid"] == pid:
            return p
    return {}

def render(current):
    print("You have " + str(playerclass.player.hp) + " HP.\n")
    print(format_passage(current["text"]))

def update(current, game_desc, choice):
    if choice == "":
        return current
    if choice == "inventory":
        print(str(playerclass.player.view_inventory()))
        option = input("Check Item, Use Item, or Back: ")
        if option == "check item":
            item = input("Which item? ")
            print(item.description)
            return current
        elif option == "use item":
            item = input("Which item? ")
            player.use_item(item)
            return current
        else:
            return current

    for i in current["links"]:
        if i["letter"] == choice:
            current = find_passage(game_desc, i["pid"])
            if "damage" in current:
                playerclass.player.hp -= current["damage"]
            return current
    print("\nInvalid choice. Please try again.")

    return current

def get_input(current):
    choice = input("\nWhat will you do? ")
    choice = choice.lower().strip()
    return choice







def main():
    game_desc = load("ADragon'sHoardV2.json")
    current = find_passage(game_desc, game_desc["startnode"])
    choice = ""
    print("\nWelcome to \"A Dragon's Hoard\"! Enter the letter of the choice you want to progress, or type 'inventory' or 'quit'.\n\n")
    while choice != "quit" and current != {}:
        current = update(current, game_desc, choice)
        render(current)
        choice = get_input(current)
    print("Thanks for playing!\n")

if __name__ == "__main__":
  main()