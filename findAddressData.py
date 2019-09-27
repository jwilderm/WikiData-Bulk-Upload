import urllib.request
import json

# This method gets the town, state, country and coordinates of the castle from nominatim/lookup
def find_address(osm_id, osm_type):
    address = ['','','','']
    fp = urllib.request.urlopen('https://nominatim.openstreetmap.org/lookup?osm_ids={osm_type}{osm_id}&format=json'.format(osm_type=osm_type.capitalize()[0],osm_id=osm_id))
    my_bytes = fp.read()
    my_string = my_bytes.decode("utf8")
    my_split = my_string.split('\n')
    fp.close()
    for line in my_split:
        if '[{' in line:
            json_data = json.loads(line[:-1][1:])
            break
    if 'town' in json_data['address']:
        address[0] = json_data['address']['town']
    elif 'village' in json_data['address']:
        address[0] = json_data['address']['village']
    elif 'city' in json_data['address']:
        address[0] = json_data['address']['city']
    else:
        address[0] = 'Nothing'
    try:
        address[1] = json_data['address']['state']
    except:
        pass
    if 'Schweiz' in json_data['address']['country'] or 'Switzerland' in json_data['address']['country']:
        address[2] = 'Switzerland'
    elif 'Deutschland' in json_data['address']['country'] or 'Germany' in json_data['address']['country']:
        address[2] = 'Germany'
    elif 'Österreich' in json_data['address']['country'] or 'Austria' in json_data['address']['country']:
        address[2] = 'Austria'
    elif 'Liechtenstein' in json_data['address']['country']:
        address[2] = 'Liechtenstein'
    elif 'Frankreich' in json_data['address']['country'] or 'France' in json_data['address']['country']:
        address[2] = 'France'
    elif 'Italien' in json_data['address']['country'] or 'Italy' in json_data['address']['country'] or 'Italia' in json_data['address']['country']:
        address[2] = 'Italy'
    address[3] = '@' + json_data['lat'] + '/' + json_data['lon']
    return address

# This method searches for the castle_type on openstreetmap
def find_type(osm_id, osm_type):
    fp = urllib.request.urlopen('https://www.openstreetmap.org/{osm_type}/{osm_id}'.format(osm_type=osm_type,osm_id=osm_id))
    my_bytes = fp.read()

    my_string = my_bytes.decode("utf8")
    my_split = my_string.split('\n')
    fp.close()

    for line in my_split:
        if '<a title="' in line and '">stately</a>' in line:
            castle_type = 'Stately'
            break
        elif '<a title="' in line and '">defensive</a>' in line:
            castle_type = 'Castle'
            break
        elif 'a title="' in line and '">manor</a>' in line:
            castle_type = 'Manor'
            break
        elif 'a title="' in line and '">fortress</a>' in line:
            castle_type = 'Fortress'
            break
        elif '<td class="browse-tag-v">tower</td>' in line:
            castle_type = 'Castle'
            break
        elif '<td class="browse-tag-v">castle</td>' in line:
            castle_type = 'Castle'
            break
        else:
            castle_type = 'Castle'
    return castle_type

# This method speculates what the language of the name of the castle is and also generates a simple description in all three languages
def get_language(name, country, castle_type):
    languages = ['', '', '', '', '', '']
    country_nr = 0
    country_de = ['Schweiz', 'Deutschland', 'Österreich', 'Frankreich', 'Italien', 'Liechtenstein']
    country_fr = ['Suisse', 'Allemagne', 'Autriche', 'France', 'Italie', 'Liechtenstein']
    country_it = ['Svizzera', 'Germania', 'Austria', 'Francia', 'Italia', 'Liechtenstein']

    type_nr = 0
    type_de = ['Burg', 'Schloss', 'Herrenhaus', 'Fort']
    type_fr = ['Château fort', 'Château', 'Maison bourgeoise', 'Fort']
    type_it = ['Castello', 'Castello', 'Magione', 'Forte']
    
    if country == 'France':
        languages[1] = name
        country_nr = 3
    elif country == 'Italy':
        languages[2] = name
        country_nr = 4
    elif country == 'Switzerland':
        languages[0] = name
        country_nr = 0
    elif country == 'Germany':
        languages[0] = name
        country_nr = 1
    elif country == 'Austria':
        languages[0] = name
        country_nr = 2
    elif country == 'Liechtenstein':
        languages[0] = name
        country_nr = 5
    
    if castle_type == 'Castle':
        type_nr = 0
    elif castle_type == 'Stately':
        type_nr = 1
    elif castle_type == 'Manor':
        type_nr = 2
    elif castle_type == 'Fortress':
        type_nr = 3

    languages[3] = f'{type_de[type_nr]}({country_de[country_nr]})'
    languages[4] = f'{type_fr[type_nr]}({country_fr[country_nr]})'
    languages[5] = f'{type_it[type_nr]}({country_it[country_nr]})'
    return languages

index = 0
# Read file and make a list of all castles
try:
    with open('Castles.txt') as f:
        castles = f.readlines()
    f.close()
except FileNotFoundError:
    print('Castles.txt not found.')

# The output is a file which contains address-data and other information of all the castles
w = open('CastleData.txt', 'w')
while index < len(castles):
    data = castles[index].split('\t', 2)
    if data[2][-1] == '\n':
        data[2] = data[2][:-1]
    if data[2] == '-':
        data[2] = ''
    address = find_address(data[0], data[1])
    castle_type = find_type(data[0], data[1])
    languages = get_language(data[2], address[2], castle_type)

    for line in languages:
        w.write(f'{line},')
    address[1] = f'{address[1]}>{address[2]}'
    address[0] = f'{address[0]}>{address[1]}'
    w.write(f'{castle_type},{address[0]},{address[1]},{address[2]},{address[3]}\n')

    index += 1
w.close()