import json

with open('Things.json') as things:
    thing = json.load(things)

print (thing)
