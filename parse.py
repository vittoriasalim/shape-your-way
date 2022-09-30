import json

def parse_json():

    # get the json config
    my_json = open("config.json",'r')

    # load into a json object
    data = json.load(my_json)

    levels = data["levels"]
    return levels

def read_map(file):
    my_file = open(file,'r')
    data = my_file.read().split("\n")
    return data

    

    