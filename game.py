import player

def playGame():
    allDead = False
    
    while True:
        for currPlayer in players:
            if currPlayer.isDead == False:
                currPlayer.turn(currPlayer=currPlayer, evilBaron=evilBaron)
                
        allDead = True;
        for currPlayer in players:
            if allDead == True and currPlayer.isDead == False: 
                allDead = False
                
        for currPlayer in players:
            if currPlayer.iWon == True:
                print ("Game Over. " + currPlayer.getTitle() + " " + currPlayer.name + " wins.")
                return
            
        if allDead == True:
            print("The game has ended.\n");
            break
