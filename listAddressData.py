# This script goes through the list of castles and finds all the referenced towns and states in which the castles are
try:
    with open('CastleData.txt', 'r') as f:
        castles = f.readlines()
    f.close()
except FileNotFoundError:
    print('CastleData.txt not found.')

index = 0
in_list = False

town_list = []
state_list = []

# If there already are some towns and states in the output-files (from previous castle-lists), this part of the script reads through these files too
try:
    with open('townList.txt', 'r') as t:
        towns = t.readlines()
    t.close()
    i = 0
    while i < len(towns) - 1:
        town_list[i] = towns[i].split(',')[0]
        i += 1
except FileNotFoundError:
    town_list = []
    towns = []

try:
    with open('stateList.txt', 'r') as s:
        states = s.readlines()
    s.close()
    i = 0
    while i < len(states) - 1:
        state_list[i] = states[i].split(',')[0]
        i += 1
except FileNotFoundError:
    state_list = []
    states = []

# This part makes sure the towns and states only appear once in the arrays, it generates no duplicates
while index < len(castles):
    castle_town = castles[index].split(',')[7]
    castle_state = castles[index].split(',')[8]
    for town in town_list:
        if town == castle_town:
            in_list = True
            break
    if in_list == False:
        town_list.append(castle_town)
    in_list = False
    for state in state_list:
        if state == castle_state:
            instate_list = True
            break
    if in_list == False:
        state_list.append(castle_state)
    in_list = False
    index += 1

# The output is two files which contain all the towns and states. The matching Q-Numbers should be added manually
w = open('townList.txt', 'w')
i = 0
while i < len(town_list):
    if i < len(towns):
        w.write(towns[i])
    else:
        w.write(town_list[i] + ',\n')
    i += 1
w.close()

v = open('stateList.txt', 'w')
i = 0
while i < len(state_list):
    if i < len(states):
        v.write(states[i])
    else:
        v.write(state_list[i] + ',\n')
    i += 1
v.close()