#This script makes it easier for the user to check if the names of the castles are the correct language and correct it
def change_lang(de, fr, it):
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
    castle_data = castles[index].split(',')

    while True:
        print('DE\tFR\tIT')
        print('-' + castle_data[0] + '\t-' + castle_data[1] + '\t-' + castle_data[2])
        controll = input('Language: DE (d), FR (f), IT (i), correct (enter)')
        if controll == 'd':
            castle_data[0] = change_lang(castle_data[0], castle_data[1], castle_data[2])
            castle_data[1] = ''
            castle_data[2] = ''
            break
        elif controll == 'f':
            castle_data[1] = change_lang(castle_data[0], castle_data[1], castle_data[2])
            castle_data[0] = ''
            castle_data[2] = ''
            break
        elif controll == 'i':
            castle_data[2] = change_lang(castle_data[0], castle_data[1], castle_data[2])
            castle_data[0] = ''
            castle_data[1] = ''
            break
        elif controll == '':
            break

    str = ','
    for data in castle_data:
        str += (data + ',')
    w.write(str[:-1])
    index += 1
w.close()