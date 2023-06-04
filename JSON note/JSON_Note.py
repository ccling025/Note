import json

person = {"name":"Amy", "age":"20", "city":"Tainan", "height":"165"},

person_json = json.dumps(person, indent=4, sort_keys=True) #json.dumps for strings #separators/indent/sort_keys
#print(person_json)
person1 = json.loads(person_json)
print(person1)

#with open("person.json", mode="w") as jfile:
    #json.dump(person, jfile, indent=4) #json.dump for files

with open(person.json, mode="r") as jfile:
    jdata = json.load(jfile)