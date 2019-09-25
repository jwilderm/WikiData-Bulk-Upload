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
  - When finished, there should be a new file "CastleData.txt" in the directory
