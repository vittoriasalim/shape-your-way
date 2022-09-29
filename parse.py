from ast import parse
import json

def parse_json():
    my_json = open("config.json",'r')
    data = json.load(my_json)

    levels = data["levels"]
    return levels

def read_map(file):
    my_file = open(file,'r')
    data = my_file.read().split("\n")
    return data

    

    