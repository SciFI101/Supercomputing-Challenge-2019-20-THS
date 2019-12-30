
#Python 3.6.5
#This is just a simple interface for the database
import csv
import json
from os import path

#csvfile = csv.DictReader(open("./database/diseaseSymptomDB.csv"))
#for row in csvfile:
#    print(row)

#print("Json Time!")

def lookup(query):
    #with open("./database/diseaseSymptomDB.json") as path:
    jsonfile = json.load(open("./database/diseaseSymptomDB.json"))
    for i in range(len(jsonfile)):
        if query.lower in jsonfile:
            return jsonfile[query]
        else:
            return "Nothin\' boss, sorry"

print(lookup("depression mental"))