import math
import pathlib, os, sys
import random
import pyttsx3


engine = pyttsx3.init()

class Node:
    def __init__(self, key):
        self.id = key
        self.connected_to = {}
        self.visited = False
        self.previous = None
        self.cardinal = ""
        self.holdsKey = False
        self.enemyType = ""
        self.exitLocation = False
        self.healStation = False
        self.startingNode = False
        self.currentNode = False
        self.curLookCard = "North"

    def __str__(self):
        tempList = self.connected_to.keys()
        tempStr = ""
        for key in tempList:
            tempStr += "Node " + str(key.id) + " " + self.connected_to[key] +", "
        return str(self.id) + ' is connected to: ' + tempStr


    def get_id(self): #return the number of the node
        return self.id

    def get_connections(self):
        return self.connected_to.keys()

    def get_cardinals(self):
        return self.connected_to.values()

    def get_enemyType(self):
        return self.enemyType

    def get_holdsKey(self):
        return self.holdsKey

    def get_healStation(self):
        return self.healStation

    def get_exitLocation(self):
        return self.exitLocation

    def set_visited(self): #maks this node as visited
        self.visited = True

    def set_previous(self): #marks the previous node 
        self.previous = prev

    def set_enemyType(self, enemyType): #0 is none, 1 is easy, 2 is hard
        if enemyType == 0:
            self.enemyType = "None"
        elif enemyType == 1:
            self.enemyType = "Easy"
        elif enemyType == 2:
            self.enemyType = "Hard"

    def set_exitLocation(self):
        self.exitLocation = True

    def set_holdsKey(self):
        self.holdsKey = True

    def set_healStation(self):
        self.healStation = True

    def set_startingNode(self):
        self.startingNode = True

###################################
    #Use these two to set or unset the current node
    def set_currentNode(self):
        self.currentNode = True

    def remove_currentNode(self):
        self.currentNode = False

    def get_currentNode(self):
        return self.currentNode

class GameLogic:
    #creates nodes
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n6 = Node(6)
    n7 = Node(7)
    n8 = Node(8)
    n11 = Node(11)
    n12 = Node(12)
    n13 = Node(13)

    #creates node connections
    n1.connected_to = {n2:"east"}
    n2.connected_to = {n1:"west", n3:"east", n7:"south"}
    n3.connected_to = {n2:"west", n8:"south"}
    n6.connected_to = {n11:"south", n7:"east"}
    n7.connected_to = {n2:"north", n6:"west", n12:"south"}
    n8.connected_to = {n3:"north"}
    n11.connected_to = {n6:"north"}
    n12.connected_to = {n7:"north", n13:"east"}
    n13.connected_to = {n12:"west"}

    print(n1)
    print(n2)
    print(n3)
    print(n6)
    print(n7)
    print(n8)
    print(n11)
    print(n12)
    print(n13)
    print("------------")
    cornerList = [1, 8, 11, 13]
    playerStartLocation = random.choice(cornerList) #gets starting location
    cornerList.remove(playerStartLocation) #removes the starting location
    endLocation = random.choice(cornerList) #this is the ending location
    cornerList.remove(endLocation)
    healLocation = random.choice(cornerList) #location of heal station
    cornerList.remove(healLocation)
    keyEnemyLocation = random.choice(cornerList) #location of emeny with key
    cornerList.remove(keyEnemyLocation)

    centerList = [2, 3, 6, 7, 12]

    hardEnemy2 = random.choice(centerList)
    centerList.remove(hardEnemy2)
    #all others should be easy enemies

    nodeList = [n1, n2, n3, n6, n7, n8, n11, n12, n13]
    for node in nodeList:
        if node.get_id() == playerStartLocation:
            print(node.get_id(), "start and current node")
            node.set_startingNode()
            node.set_currentNode()
            node.set_enemyType(0)
        if node.get_id() == endLocation:
            print(node.get_id(), "exit")
            node.set_exitLocation()
            node.set_enemyType(0)
        if node.get_id() == keyEnemyLocation: #working
            print(node.get_id(), "key enemy")
            node.set_holdsKey()
            node.set_enemyType(2)
        if node.get_id() == hardEnemy2: #working
            print(node.get_id(), "hard enemy")
            node.set_enemyType(2)
        if node.get_id() in centerList: #working
            print(node.get_id(), "easy enemy")
            node.set_enemyType(1)
        if node.get_id() == healLocation: #working
            print(node.get_id(), "heal station")
            node.set_healStation()
            node.set_enemyType(0)

    print("------------")
    print("Beginning Game Sequence")

    #initializing player health and that they dont have the key
    playerHealth = 80
    hasKey = False
    playerNode = Node(None)
    for node in nodeList: #finds which node the player is currently on
        if node.get_currentNode() == True:
            playerNode = node
            
    move = 0
    def mainGame():
        if GameLogic.move < 20: #number of turns before the player loses, was thinking 15 for 

            
            for node in GameLogic.nodeList: #finds which node the player is currently on
                if node.get_currentNode() == True:
                    GameLogic.playerNode = node
                    #playerNode = n3

            print("The player is currently on node", GameLogic.playerNode.get_id())
            #-----------------------------------------------------------------------------#
            #enemy fighting logic - COMPLETE
            if GameLogic.playerNode.get_enemyType() == "Easy" or GameLogic.playerNode.get_enemyType() == "Hard":
                engine.say("Enemy encountered, would you like to fight or run?")
                engine.runAndWait()
                print("Enemy encountered, would you like to fight or run")
                breakout = False
                userInput = input("Fight or Run?") #will be voice based
                #user enters their choice
                invalidInput = True
                while (invalidInput):
                    if userInput == "run": 
                        num = random.randint(1, 4)
                        if num == 1:
                            engine.say("You didnt escape successfully, you must fight")
                            engine.runAndWait()
                            print("You didnt escape successfully, you must fight")
                            userInput = "fight"
                        else: #teleporting case
                            engine.say("Escaped successfully")
                            engine.runAndWait()
                            print("Escaped successfully")
                            teleportTo = random.choice(GameLogic.nodeList)
                            print("Teleported to node", teleportTo.get_id())
                            teleportTo.set_currentNode()
                            GameLogic.playerNode = teleportTo
                            invalidInput = False
                            

                    elif userInput == "fight":
                        if GameLogic.playerNode.get_enemyType() == "Easy": #easy enemy case
                            engine.say("This should be a breeze (easy enemy)")
                            engine.runAndWait()
                            print("This should be a breeze (easy enemy)")
                            hurt = random.randint(5, 15)
                            GameLogic.playerHealth -= hurt
                            if GameLogic.playerNode.get_holdsKey() == True:
                                engine.say("You got a key!")
                                engine.runAndWait()
                                print("you got a key!")
                                GameLogic.hasKey = True
                            if GameLogic.playerHealth > 0:
                                engine.say("You survived with" + str(GameLogic.playerHealth) + "health!")
                                engine.runAndWait()
                                print("You survived with", str(GameLogic.playerHealth), "health!")
                                GameLogic.playerNode.set_enemyType(0)
                            else:
                                engine.say("You died, game over :(")
                                engine.runAndWait()
                                print("You died, game over :(")
                                exit()
                        if GameLogic.playerNode.get_enemyType() == "Hard": #hard enemy case
                            engine.say("Uh oh, he looks scary (hard enemy)")
                            engine.runAndWait()
                            print("Uh oh, he looks scary (hard enemy)")
                            hurt = random.randint(10, 30)
                            GameLogic.playerHealth -= hurt
                            if GameLogic.playerNode.get_holdsKey() == True:
                                engine.say("you got a key!")
                                engine.runAndWait()
                                print("you got a key!")
                                GameLogic.hasKey = True
                            if GameLogic.playerHealth > 0:
                                engine.say("You survived with" + str(GameLogic.playerHealth) + "health!")
                                engine.runAndWait()
                                print("You survived with", str(GameLogic.playerHealth), "health!")
                                GameLogic.playerNode.set_enemyType(0)
                            else:
                                engine.say("You died, game over :(")
                                engine.runAndWait()
                                print("You died, game over :(")
                                exit()
                        invalidInput = False
                    else:
                        engine.say("Enemy encountered, would you like to fight or run")
                        engine.runAndWait()
                        print("Enemy encountered, would you like to fight or run")
                        userInput = "fight" #will be voice based
                        invalidInput = True
            #-----------------------------------------------------------------------------#
            #heal station logic - COMPLETE        

            if GameLogic.playerNode.get_healStation() == True:
                engine.say("Youve encountered a heal station! Healing you now.")
                engine.runAndWait()
                print("Youve encountered a heal station! Healing you now.")
                GameLogic.playerHealth = 60
                engine.say("Current health:" + str(GameLogic.playerHealth))
                engine.runAndWait()
                print("Current health:", GameLogic.playerHealth)

            #-----------------------------------------------------------------------------#
            #endgame logic - COMPLETE
                
            if GameLogic.playerNode.get_exitLocation() == True:
                if GameLogic.hasKey == True:
                    engine.say("Youve escaped! You win!")
                    engine.runAndWait()
                    print("Youve escaped! You win!")
                    exit()
                else:
                    engine.say("Youve found the exit but don't have the key! Go find it!")
                    engine.runAndWait()
                    print("Youve found the exit but don't have the key! Go find it!")
                
            #-----------------------------------------------------------------------------#
            #movement logic - NEEDS WORK
            validDirections = list(GameLogic.playerNode.get_cardinals())
            validNodes = list(GameLogic.playerNode.get_connections())
            engine.say("I see a path to the: ")
            engine.runAndWait()
            print("I see a path to the: ")
            for i in range(len(validDirections)):
                print(validDirections[i])
                engine.say(validDirections[i])
            print("Which direction would you like to go in?")
            engine.say("Which direction would you like to go in?")
            engine.runAndWait()
            GameLogic.playerNode.remove_currentNode()
            #userInput = validDirections[0] # Test the first choice
            flag = True
            while flag:
                userInput = input("Enter Direction: ")
                print(userInput) # print
                if userInput in validDirections:
                    flag = False
                else:
                    engine.say("This is not a valid direction, please choose again")
                    engine.runAndWait()
                    print("This is not a valid direction, please choose again")
                    
            print("Going to " + str(validNodes[validDirections.index(userInput)].get_id())) # use validNodes[validDirections.index(userInput)].get_id() to get the node id/node key
            GameLogic.playerNode = validNodes[validDirections.index(userInput)]
            GameLogic.playerNode.set_currentNode()
            GameLogic.playerNode.curLookCard = userInput.capitalize()
            engine.say("Looking " + GameLogic.playerNode.curLookCard)
            engine.runAndWait()
            print("Looking " + GameLogic.playerNode.curLookCard)
            GameLogic.move += 1
            print("moves taken: ", GameLogic.move)
            GameLogic.mainGame()
        else:
            engine.say("Uh oh, you ran out of moves, you lose!!! loser, loser, loser hahahaha")
            engine.runAndWait()
            print("player has lost....took too many moves")
            exit()

GameLogic.mainGame()
