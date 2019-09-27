import urllib.request
import webbrowser
import requests

#This script makes it easier for the user to reference the correct WikiData-item on the OSM-Entry
with open("CastleUpload.csv") as f:
  lineList = f.readlines()
f.close()

#Gets the index from a file
try:
    with open('temp.txt') as t:
        index = t.readline()
        index = int(index)
    t.close()
#If the file has not been created yet, the index is 1
except:
    index = 1

while index < len(lineList):
    print('Current index= ' + str(index))
    data = lineList[index].split(',')
    coordX = data[-1].split('/')[0][1:]
    coordY = data[-1].split('/')[1][:-1]

    #Opens all the WikiData-items 100 meters near the given coordinates in new browser-tabs
    url = 'https://query.wikidata.org/sparql'
    query = 'SELECT * WHERE {SERVICE wikibase:around {?place wdt:P625 ?location .bd:serviceParam wikibase:center "Point('+coordY+' '+coordX+')"^^geo:wktLiteral .bd:serviceParam wikibase:radius "0.1".}}'
    r = requests.get(url, params = {'format': 'json', 'query': query})
    
    try:
        dataJson = r.json()
    except:
        exec(open('u:/Desktop/burgegschmeus/wikiDataFinder.py').read())

    amount_of_results = len(dataJson['results']['bindings'])
    
    if(amount_of_results > 0):
        for f in dataJson['results']['bindings']:
            webbrowser.open_new_tab(f['place']['value'])
    else:
        print('no results found')

    #On a new browser-tab, the edit-page of osm opens on the given coordinates
    webbrowser.open_new_tab('https://www.openstreetmap.org/edit#map=19/' + coordX[:8] + '/' + coordY[:7])

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