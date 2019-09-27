import urllib.request
import json

country_de = {
    'Switzerland': 'Schweiz',
    'Germany': 'Deutschland',
    'Austria': 'Österreich',
    'France': 'Frankreich',
    'Italy': 'Italien',
    'Liechtenstein': 'Liechtenstein'
}

country_fr = {
    'Switzerland': 'Suisse',
    'Germany': 'Allemagne',
    'Austria': 'Autriche',
    'France': 'France',
    'Italy': 'Italie',
    'Liechtenstein': 'Liechtenstein'
}

country_it = {
    'Switzerland': 'Svizzera',
    'Germany': 'Germania',
    'Austria': 'Austria',
    'France': 'Francia',
    'Italy': 'Italia',
    'Liechtenstein': 'Liechtenstein'
}

type_de = {
    'Castle': 'Burg',
    'Stately': 'Schloss',
    'Manor': 'Herrenhaus',
    'Fortress': 'Fort'
}

type_fr = {
    'Castle': 'Château fort',
    'Stately': 'Château',
    'Manor': 'Maison bourgeoise',
    'Fortress': 'Fort'
}

type_it = {
    'Castle': 'Castello',
    'Stately': 'Castello',
    'Manor': 'Magione',
    'Fortress': 'Forte'
}

# This method gets the town, state, country and coordinates of the castle from nominatim/lookup
def find_address(osm_id, osm_type):
    address = ['','','','']
    my_split = read_html('https://nominatim.openstreetmap.org/lookup?osm_ids={osm_type}{osm_id}&format=json'.format(osm_type=osm_type.capitalize()[0],osm_id=osm_id))

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
    my_split = read_html(f'https://www.openstreetmap.org/{osm_type}/{osm_id}')

    for line in my_split:
        if '<a title="' in line and '">stately</a>' in line:
            castle_type = 'Stately'
            break
        elif 'a title="' in line and '">manor</a>' in line:
            castle_type = 'Manor'
            break
        elif 'a title="' in line and '">fortress</a>' in line:
            castle_type = 'Fortress'
            break
        else:
            castle_type = 'Castle'
    return castle_type

# This method speculates what the language of the name of the castle is and also generates a simple description in all three languages
def get_language(name, country, castle_type):
    languages = ['', '', '', '', '', '']
    
    if country == 'France':
        languages[1] = name
    elif country == 'Italy':
        languages[2] = name
    else:
        languages[0] = name

    languages[3] = f'{type_de[castle_type]}({country_de[country]})'
    languages[4] = f'{type_fr[castle_type]}({country_fr[country]})'
    languages[5] = f'{type_it[castle_type]}({country_it[country]})'
    return languages

# Split lines of the html from the request
def read_html(url):
    fp = urllib.request.urlopen(url)
    my_bytes = fp.read()
    fp.close()
    my_string = my_bytes.decode("utf8")
    return my_string.split('\n')
    
index = 0
# Read file and make a list of all castles
try:
    with open('Castles.txt') as f:
        castles = f.readlines()
    f.close()
except FileNotFoundError:
    print('Castles.txt not found.')

# The output is a file which contains address-data and other information of all the castles
with open('CastleData.txt', 'w') as w:
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