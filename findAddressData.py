import urllib.request
import json

# This method gets the town, state, country and coordinates of the castle from nominatim/lookup
def findAddress(osmID, osmType):
    address = ['','','','']
    fp = urllib.request.urlopen('https://nominatim.openstreetmap.org/lookup?osm_ids={osmType}{osmID}&format=json'.format(osmType=osmType.capitalize()[0],osmID=osmID))
    mybytes = fp.read()
    mystr = mybytes.decode("utf8")
    mySplit = mystr.split('\n')
    fp.close()
    for line in mySplit:
        if '[{' in line:
            jsonData = json.loads(line[:-1][1:])
            break
    if 'town' in jsonData['address']:
        address[0] = jsonData['address']['town']
    elif 'village' in jsonData['address']:
        address[0] = jsonData['address']['village']
    elif 'city' in jsonData['address']:
        address[0] = jsonData['address']['city']
    else:
        address[0] = 'Nothing'
    try:
        address[1] = jsonData['address']['state']
    except:
        pass
    if 'Schweiz' in jsonData['address']['country'] or 'Switzerland' in jsonData['address']['country']:
        address[2] = 'Switzerland'
    elif 'Deutschland' in jsonData['address']['country'] or 'Germany' in jsonData['address']['country']:
        address[2] = 'Germany'
    elif 'Österreich' in jsonData['address']['country'] or 'Austria' in jsonData['address']['country']:
        address[2] = 'Austria'
    elif 'Liechtenstein' in jsonData['address']['country']:
        address[2] = 'Liechtenstein'
    elif 'Frankreich' in jsonData['address']['country'] or 'France' in jsonData['address']['country']:
        address[2] = 'France'
    elif 'Italien' in jsonData['address']['country'] or 'Italy' in jsonData['address']['country'] or 'Italia' in jsonData['address']['country']:
        address[2] = 'Italy'
    address[3] = '@' + jsonData['lat'] + '/' + jsonData['lon']
    return address

# This method searches for the castletype on openstreetmap
def findType(osmID, osmType):
    fp = urllib.request.urlopen('https://www.openstreetmap.org/{osmType}/{osmID}'.format(osmType=osmType,osmID=osmID))
    mybytes = fp.read()

    mystr = mybytes.decode("utf8")
    mySplit = mystr.split('\n')
    fp.close()

    for line in mySplit:
        if '<a title="' in line and '">stately</a>' in line:
            castleType = 'Stately'
            break
        elif '<a title="' in line and '">defensive</a>' in line:
            castleType = 'Castle'
            break
        elif 'a title="' in line and '">manor</a>' in line:
            castleType = 'Manor'
            break
        elif 'a title="' in line and '">fortress</a>' in line:
            castleType = 'Fortress'
            break
        elif '<td class="browse-tag-v">tower</td>' in line:
            castleType = 'Castle'
            break
        elif '<td class="browse-tag-v">castle</td>' in line:
            castleType = 'Castle'
            break
        else:
            castleType = 'Castle'
    return castleType

# This method speculates what the language of the name of the castle is and also generates a simple description in all three languages
def getLanguage(name, country, castleType):
    languages = ['', '', '', '', '', '']
    countrynr = 0
    countryde = ['Schweiz', 'Deutschland', 'Österreich', 'Frankreich', 'Italien', 'Liechtenstein']
    countryfr = ['Suisse', 'Allemagne', 'Autriche', 'France', 'Italie', 'Liechtenstein']
    countryit = ['Svizzera', 'Germania', 'Austria', 'Francia', 'Italia', 'Liechtenstein']

    typenr = 0
    typede = ['Burg', 'Schloss', 'Herrenhaus', 'Fort']
    typefr = ['Château fort', 'Château', 'Maison bourgeoise', 'Fort']
    typeit = ['Castello', 'Castello', 'Magione', 'Forte']
    
    if country == 'France':
        languages[1] = name
        countrynr = 3
    elif country == 'Italy':
        languages[2] = name
        countrynr = 4
    elif country == 'Switzerland':
        languages[0] = name
        countrynr = 0
    elif country == 'Germany':
        languages[0] = name
        countrynr = 1
    elif country == 'Austria':
        languages[0] = name
        countrynr = 2
    elif country == 'Liechtenstein':
        languages[0] = name
        countrynr = 5
    
    if castleType == 'Castle':
        typenr = 0
    elif castleType == 'Stately':
        typenr = 1
    elif castleType == 'Manor':
        typenr = 2
    elif castleType == 'Fortress':
        typenr = 3

    languages[3] = typede[typenr] + ' (' + countryde[countrynr] + ')'
    languages[4] = typefr[typenr] + ' (' + countryfr[countrynr] + ')'
    languages[5] = typeit[typenr] + ' (' + countryit[countrynr] + ')'
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
    address = findAddress(data[0], data[1])
    castleType = findType(data[0], data[1])
    languages = getLanguage(data[2], address[2], castleType)

    for line in languages:
        w.write(line + ',')
    address[1] = address[1] + '>' + address[2]
    address[0] = address[0] + '>' + address[1]
    w.write(castleType + ',' + address[0] + ',' + address[1] + ',' + address[2] + ',' + address[3] + '\n')

    index += 1
w.close()