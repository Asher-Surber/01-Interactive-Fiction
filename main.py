#!/usr/bin/env python3
import sys, os, json, re
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
    return description

def find_passage(game_desc, pid):
    for p in game_desc["passages"]:
        if p[pid] == pid:
            return p
    return {}

def render(current):
    print(current["name"])
    print(current["text"])

def update(current, game_desc, choice):
    if choice == "":
        return current
    for i in current["links"]:
        if i["name"] == choice:
            current = find_passage(game_desc, i[pid])
            return current
    print("Invalid choice. Please try again.")
    return current

def get_input(current):
    choice = input("What will you do? ")
    return choice






def main():
  game_desc = load("game.json")
  current = find_passage(game_desc, game_desc["startnode"])
  choice = ""

if __name__ == "__main__":
  main()