#This script makes it easier for the user to check if the names of the castles are the correct language and correct it
def changeLang(de, fr, it):
    if de != '':
        return de
    elif fr != '':
        return fr
    else:
        return it

try:
    with open('CastleData.txt', 'r') as f:
        castles = f.readlines()
    f.close()
except FileNotFoundError:
    print('CastleData.txt not found.')

index = 0

w = open('CastleUpload.csv', 'w')
w.write('qid,Lde,Lfr,Lit,Dde,Dfr,Dit,P31,P131,P131,P17,P625\n')
while index < len(castles):
    print(castles[index])
    castleData = castles[index].split(',')
    print('DE\tFR\tIT')
    print('-' + castleData[0] + '\t-' + castleData[1] + '\t-' + castleData[2])
    controll = input('Language: DE (d), FR (f), IT (i), correct (enter)')

    while True:
        if controll == 'd':
            castleData[0] = changeLang(castleData[0], castleData[1], castleData[2])
            castleData[1] = ''
            castleData[2] = ''
            break
        elif controll == 'f':
            castleData[1] = changeLang(castleData[0], castleData[1], castleData[2])
            castleData[0] = ''
            castleData[2] = ''
            break
        elif controll == 'i':
            castleData[2] = changeLang(castleData[0], castleData[1], castleData[2])
            castleData[0] = ''
            castleData[1] = ''
            break
        elif controll == '':
            break

    str = ','
    for data in castleData:
        str += (data + ',')
    w.write(str[:-1])
    index += 1
w.close()