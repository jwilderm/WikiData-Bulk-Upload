# WikiData-Bulk-Upload
This repository contains python-scripts which helps one to create a list of WikiData-Items of castles and towers

## The steps you take for uploading a bunch of castles to WikiData
- Get the castles from OSM into a text-file
  - Go to https://meta.wikimedia.org/wiki/Wikimedia_CH/Burgen-Dossier/FehlendeWikidataReferenzen
  - Copy all the data from the table (ID, Type, Name)
  - Paste the data into a txt-file named "Castles.txt". Move the file into the directory "WikiData-Bulk-Upload"
- Get the needed data for the castles from the internet
  - Run the script "findAddressData.py"
  - Dont worry if you think the script takes too much time. If your "Castles.txt" contains a large amount of castles, the script may take a few minutes to get all the address-data from the internet.
  - When finished, there should be a new file "CastleData.txt" in the directory, which contains the names in one of three languages (DE, FR, IT), descriptions in all three languages, castle-types, towns, states, countries and coordinates of the castles.
- Replace data with matching Q-Numbers from WikiData
  - Run the script "listAddressData.py"
  - It goes through "CastleData.txt" and extends "townList.txt" and "stateList.txt" with towns and states which appear in CastleData but don't exist in the lists yet. "countryList.txt" and "typeList.txt" already are complete.
  - The script will crash if you execute it but townList or stateList contain data with no matching Q-Number next to the ",".
  - Open "townList.txt" and "stateList.txt". Fill in matching Q-Numbers from https://www.wikidata.org/wiki/Wikidata:Main_Page next to the commas of the containing data (no whitespaces between). Make sure all the towns and states have their Q-Number before you continue.
  - Run the script "QNumberConverter.py"
  - It replaces all the castle-types, towns, states and countries in "CastleData.txt" with the matching Q-Numbers in the four list-files.
