from sys import argv
import requests
import json


def getData(miner): # miner =  eth adr. used
    parameters = "miner/%s/dashboard" % miner
    response  = requests.get('https://api.ethermine.org/%s' % parameters)
    return response

data = getData(str(argv[1]))
dataAsJSON = data.json()
print(dataAsJSON)