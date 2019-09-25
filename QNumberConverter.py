#This script opens the castle-list and replaces all castle-types, towns, states and country with their Q-Number
with open('CastleData.txt', 'r') as f:
    castles = f.readlines()
f.close()

with open('townList.txt', 'r') as f:
    towns = f.readlines()
f.close()

with open('stateList.txt', 'r') as f:
    states = f.readlines()
f.close()

with open('countryList.txt', 'r') as f:
    countries = f.readlines()
f.close()

with open('typeList.txt', 'r') as f:
    types = f.readlines()
f.close()

index = 0
w = open('CastleData.txt', 'w')

while index < len(castles):
    castleData = castles[index].split(',')
    for town in towns:
        if town.split(',')[0] == castleData[7]:
            castleData[7] = town.split(',')[1][:-1]
            break
    if castleData[8] != '':
        for state in states:
            if state.split(',')[0] == castleData[8]:
                castleData[8] = state.split(',')[1][:-1]
                break
    for country in countries:
        if country.split(',')[0] == castleData[9]:
            castleData[9] = country.split(',')[1][:-1]
            break
    for type in types:
        if type.split(',')[0] == castleData[6]:
            castleData[6] = type.split(',')[1][:-1]
            break
    str = ''
    for data in castleData:
        str += (data + ',')
    w.write(str[:-1])
    index += 1
w.close()