import sys

class ListIncompleteError(Exception):
    """Raised when one of the four lists are incomplete"""
    pass

#This script opens the castle-list and replaces all castle-types, towns, states and country with their Q-Number
try:
    with open('CastleData.txt', 'r') as f:
        castles = f.readlines()
    f.close()
except FileNotFoundError:
    print('CastleData.txt not found.')
try:
    with open('townList.txt', 'r') as f:
        towns = f.readlines()
    f.close()
except FileNotFoundError:
    print('townList.txt not found.')
try:
    with open('stateList.txt', 'r') as f:
        states = f.readlines()
    f.close()
except FileNotFoundError:
    print('stateList.txt not found.')
try:
    with open('countryList.txt', 'r') as f:
        countries = f.readlines()
    f.close()
except FileNotFoundError:
    print('countryList.txt not found.')
try:
    with open('typeList.txt', 'r') as f:
        types = f.readlines()
    f.close()
except FileNotFoundError:
    print('typeList.txt not found.')

index = 0
try:
    w = open('CastleData.txt', 'w')
    while index < len(castles):
        castleData = castles[index].split(',')
        for town in towns:
            if town.split(',')[0] == castleData[7]:
                castleData[7] = town.split(',')[1][:-1]
                if castleData[7] == '':
                    print('townList.txt is incomplete. Make sure it is before you proceed.')
                    raise ListIncompleteError
                break
        if castleData[8] != '':
            for state in states:
                if state.split(',')[0] == castleData[8]:
                    castleData[8] = state.split(',')[1][:-1]
                    if castleData[8] == '':
                        print('stateList.txt is incomplete. Make sure it is before you proceed.')
                        raise ListIncompleteError
                    break
        for country in countries:
            if country.split(',')[0] == castleData[9]:
                castleData[9] = country.split(',')[1][:-1]
                if castleData[9] == '':
                    print('countryList.txt is incomplete. Make sure it is before you proceed.')
                    raise ListIncompleteError
                break
        for type in types:
            if type.split(',')[0] == castleData[6]:
                castleData[6] = type.split(',')[1][:-1]
                if castleData[6] == '':
                    print('typeList.txt is incomplete. Make sure it is before you proceed.')
                    raise ListIncompleteError
                break
        str = ''
        for data in castleData:
            str += (data + ',')
        w.write(str[:-1])
        index += 1
except ListIncompleteError:
    for line in castles:
        w.write(line)
finally:
    w.close()