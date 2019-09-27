import urllib.request
import webbrowser
import requests

#This script makes it easier for the user to reference the correct WikiData-item on the OSM-Entry
try:
    with open("CastleUpload.csv") as f:
        castles = f.readlines()
    f.close()
except FileNotFoundError:
    print('CastleUpload.csv not found.')

#Gets the index from a file
try:
    with open('temp.txt') as t:
        index = t.readline()
        index = int(index)
    t.close()
#If the file has not been created yet, the index is 1
except:
    index = 1

while index < len(castles):
    print('Current index= ' + str(index))
    data = castles[index].split(',')
    coordinates_x = data[-1].split('/')[0][1:]
    coordinates_y = data[-1].split('/')[1][:-1]

    #Opens all the WikiData-items 100 meters near the given coordinates in new browser-tabs
    url = 'https://query.wikidata.org/sparql'
    query = 'SELECT * WHERE {SERVICE wikibase:around {?place wdt:P625 ?location .bd:serviceParam wikibase:center "Point('+coordinates_y+' '+coordinates_x+')"^^geo:wktLiteral .bd:serviceParam wikibase:radius "0.1".}}'
    r = requests.get(url, params = {'format': 'json', 'query': query})
    
    try:
        json_data = r.json()
    except:
        exec(open('u:/Desktop/burgegschmeus/wikiDataFinder.py').read())

    amount_of_results = len(json_data['results']['bindings'])
    
    if(amount_of_results > 0):
        for f in json_data['results']['bindings']:
            webbrowser.open_new_tab(f['place']['value'])
    else:
        print('no results found')

    #On a new browser-tab, the edit-page of osm opens on the given coordinates
    webbrowser.open_new_tab('https://www.openstreetmap.org/edit#map=19/' + coordinates_x[:8] + '/' + coordinates_y[:7])

    #Asks the user to continue with the next castle and saves the index in a file
    controller = input('Continue? Yes = Enter, No = Other input: ')
    if controller != '':
        break
    index += 1
    w = open('temp.txt', 'w')
    w.write(str(index))
    w.close()

w = open('temp.txt', 'w')
w.write('1')
w.close()