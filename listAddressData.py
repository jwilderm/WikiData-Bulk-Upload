# This script goes through the list of castles and finds all the referenced towns and states in which the castles are
with open('CastleData.txt', 'r') as f:
    castles = f.readlines()
f.close()

index = 0
inTownList = False
inStateList = False

townList = []
townQs = []
stateList = []
stateQs = []

# If there already are some towns and states in the output-files (from previous castle-lists), this part of the script reads through these files too
try:
    with open('townList.txt', 'r') as t:
        towns = t.readlines()
    t.close()
    i = 0
    while i < len(towns):
        townList[i] = towns[i].split(',')[0]
        townQs[i] = towns[i].split(',')[1]
        i += 1
except FileNotFoundError:
    townList = []

try:
    with open('stateList.txt', 'r') as s:
        states = s.readlines()
    s.close()
    i = 0
    while i < len(states):
        stateList[i] = states[i].split(',')[0]
        stateQs[i] = states[i].split(',')[1]
        i += 1
except FileNotFoundError:
    stateList = []

# This part makes sure the towns and states only appear once in the arrays, it generates no duplicates
while index < len(castles):
    castleTown = castles[index].split(',')[7]
    castleState = castles[index].split(',')[8]
    for town in townList:
        if town == castleTown:
            inTownList = True
            break
    if inTownList == False:
        townList.append(castleTown)
    for state in stateList:
        if state == castleState:
            inStateList = True
            break
    if inStateList == False:
        stateList.append(castleState)
    inTownList = False
    inStateList = False
    index += 1

# The output is two files which contain all the towns and states. The matching Q-Numbers should be added manually
w = open('townList.txt', 'w')
i = 0
while i < len(townList):
    if i < len(townQs):
        w.write(townList[i] + ',' + townQs[i] + '\n')
    else:
        w.write(townList[i] + ',\n')
    i += 1
w.close()

v = open('stateList.txt', 'w')
i = 0
while i < len(stateList):
    if i < len(stateQs):
        v.write(stateList[i] + ',' + stateQs[i] + '\n')
    else:
        v.write(stateList[i] + ',\n')
    i += 1
v.close()