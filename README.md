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
- Make sure the languages of the names of the castles are correct
  - The names of the castles in "CastleData.txt" may be in the incorrect position. (Name-DE,Name-FR,Name-IT,...)
  - You have to correct that issue manually, but the script "languageConverter.py" can help you with that.
  - When you execute it, it displays all the castles step by step. You'll see if the name is at the correct position or not. The script allows you to correct it if necessary before it proceeds to display the following castle.
  - When the script finishes iterating through all the castles, it creates a new file "CastleUpload.csv". If there somehow already is such a file, it'll get overwritten.
- Generate the WikiData-items
  - Copy all the data from "CastleUpload.csv".
  - Go to https://tools.wmflabs.org/quickstatements/#/batch. (You need an account to be able to create WikiData-items)
  - Paste the data into the text-box and click on "Import CSV commands"
  - Click "Run" or "Run in background". It should generate one WikiData-item for each castle.
- Reference the WikiData-items in the matching OSM-entries
  - Run the script "wikiDataFinder.py"
  - It iterates through "CastleUpload.csv", gets the coordinates from a castle and opens new browser-tabs:
    - Openstreetsmap in edit-mode on the given coordinates (You also need an account for that)
    - All WikiData-items 100 meters near the given coordinates
  - If you're sure the castle on OSM and the WikiData-item match, reference the item on the OSM-entry. Press Enter to proceed with the following castle until you're done.
