import urllib2

def kwargit(stringy):
    nuStringy = stringy.split()
    retD = {}
    for item in nuStringy:
        nuItem = item.split("=")
        print nuItem
        retD[nuItem[0]] = nuItem[1]
    return retD

def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

def lowerParse(smallString):
    quoteSpots = find(smallString,'"')
    s = 0
    leng = len(quoteSpots)
    rdict = {}
    lastPos = 7
    while s < leng:
        rdict[smallString[lastPos:quoteSpots[s]-1]] = smallString[quoteSpots[s]+1:quoteSpots[s+1]]
        try: lastPos = quoteSpots[s+1]+2
        except: break
        s +=2
    return rdict

def parse(wholeString):
    nuString = wholeString.split('><')
    retDict = {}
    for item in nuString[1:-1]:
        info = lowerParse(item)
        retDict[int(info['id'])] = info
    return retDict

hiPage =urllib2.urlopen("http://uni120.ogame.org/api/players.xml")
hiPage.readline()
hiScoreDict = {}
scores = hiPage.readline()
Players = parse(scores)
playerNames = {}
for Player in Players:
    playerNames[Players[Player]['name']] = Player
hiScores = range(8)
for typed in hiScores:
    HiScores = urllib2.urlopen("http://uni120.ogame.org/api/highscore.xml?category=1&type=%i" %(typed))
    HiScores.readline()
    thisScores = parse(HiScores.readline())
    for Player in thisScores:
        infos = thisScores[Player]
        try: Players[Player]['hiScores'][typed] = (infos['position'],infos['score'])
        except: 
            try: Players[Player]['hiScores'] = {typed:(infos['position'],infos['score'])}
            except: pass
allyHiPage =urllib2.urlopen("http://uni120.ogame.org/api/alliances.xml")
