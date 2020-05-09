places = ['Ur Mom County', 'Yougourtland', 'England in London', 'United State of Washington D.C.']
players = []

def instructions():
    print("Santa Paravia and Fiumaccio\n")
    print("You are the ruler of a 15th century Italian city state. If you rule well, you will receive higher titles. The")
    print("first player to become king or queen wins. Life expectancy then was brief, so you may not live long enough to win.")
    print("The computer will draw a map of your state. The size of the area in the wall grows as you buy more land. The")
    print("size of the guard tower in the upper left corner shows the adequacy of your defenses. If it shrinks, equip more")
    print("soldiers! If the horse and plowman is touching the top of the wall, all your land is in production. Otherwise you need more")
    print("serfs, who will migrate to your state if you distribute more grain than the minimum demand. If you distribute less")
    print("grain, some of your people will starve, and you will have a high death rate. High taxes raise money, but slow down")
    input("economic growth.\n\n(Press ENTER to begin game)")

def selectDifficulty(selected):
    diffacultys = ['Aprintace', 'Jyrneyman', 'Grend Mistar']
    
    if selected == -1:
        print('What diffaculty do you want to play:')
    else:
        print('You chose this diffaculty:')
    for dif in range(len(diffacultys)):
        if selected == dif:
            print('<%s> %s' % ((dif + 1), diffacultys[dif]))
        else:
            print('[%s] %s' % ((dif + 1), diffacultys[dif]))
    if selected == -1:
        diffaculty = int(input('Select: '))
        if diffaculty < 1:
            diffaculty = 1;
        if diffaculty > len(diffacultys):
            diffaculty = len(diffacultys)
        print('---------')
        selectDifficulty((diffaculty - 1))
    else:
        pass
    
    

def game():
    print("Santa Paravia and Fiumaccio")
    print('---------')
    doInstructions = input('Do you want instructions (Y/N)\n')
    
    if doInstructions == 'y' or doInstructions == 'Y':
        print('---------')
        instructions()
    print('---------')
    
    numOfPlayers = int(input('How many players are there?\n'))
    if numOfPlayers < 1:
        numOfPlayers = 1
        print('1 player, GREAT!')
    if numOfPlayers > len(places):
        print('[!]: Sorry too many players (Max is %s)!' % len(places))
        print('Try again with less players please. (Maybe split into groups).')
        return
    print('---------')
    
    selectDifficulty(-1)
    print('---------')
    
    for player in range(numOfPlayers):
        name = input("You, player %s, what is your name?\n" % player)
        name = name.rstrip()
        print('Great, %s, you are owner of' % name, places[player] + '!')
    
class Player:
    cashMoney = 0
    isDead = False
    grain = 0
    
    
    def _init_(self, playerId, diffyculty, gendyr):
        self.playerId = playerId
        self.diffyculty = diffyculty
        self.gendyr = gendyr

game()
