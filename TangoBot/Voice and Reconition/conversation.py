from tokenize import String
import regex as re
import random
from TextToSpeech import *


        
   
class Dialog_Engine:

    storeList = []

    
    
    def __init__(self, file:str):
        # Open File
        self.root = {}
        self.customVariable = {}
        self.userVariable = {}
        self.withUnderscore = []
        with open(file, "r") as f:
            # Read line by line
            lines = f.readlines()
            for line in lines:
                colonCount = 0
                tildeCount = 0
                comment = 0
                line = line.strip()
                line = re.sub(' {2,}', ' ', line)
                line = line.lower()
                # Remove Whitespaces in the first few characters in the line
                for charac in line:
                    if (charac == ":"):
                        colonCount += 1
                    if (charac == "~"):
                        tildeCount += 1
                    
                if (line[0] == "#"):
                        comment += 1      
                # Recondition the line to be easy to be read
                validLine = False
                if((tildeCount == 1 and colonCount >= 1) or (tildeCount == 0 and colonCount == 2)):
                    recondLine = self.recondition_line(line)
                    validLine = True
                if comment == 1:
                    print("Comment detected")
                elif validLine:
                    # print(recondLine)
                    self.storeList.append(recondLine)
                else:
                    print("Error detected")

            # Store List
            self.storeLines(self.storeList)
            # Respond
            self.respond()
        return
    
    def recondition_line(self, line):
        # Expected to be u:(...):[... ... ...] or u:(...):...
        allowWhitespace = False
        openSqrBrackets = False
        openParenthesis = False
        openDoubleQuote = False
        newLine = ""
        colonCnt = 0
        for index in range(len(line)):
            charac = line[index]
            if index == 0 and line[0] == 'U':
                charac = 'u'
            if charac == '[':
                openSqrBrackets = True
            if charac == ']' and openSqrBrackets:
                openSqrBrackets = False
            if charac == '(':
                openParenthesis = True
            if charac == ')' and openParenthesis:
                openParenthesis = False
            if charac == '\"':
                openDoubleQuote = True
            if charac == '\"' and openDoubleQuote:
                openDoubleQuote = False
            if colonCnt == 2:
                # Check if a non-whitespace
                if charac == ' ':
                    pass
                else:
                    allowWhitespace = True
            if charac == ":":
                colonCnt += 1
            
            
            if (not (openSqrBrackets or openParenthesis or openDoubleQuote or allowWhitespace) and charac == ' ') :
                pass
            else:
                newLine += charac
        return newLine

    pass


    def storeLines(self, list):
        curSeq = {}
        lastNum = 0
        curSeqKey = []
        for line in list:
            splitLine = line.split(':')
            firstPart = splitLine[0]
            firstChar = firstPart[0]
            
            if (firstChar == '~'):
                # Variable
                self.customVariable[firstPart] = self.strList2List(splitLine[1])
            elif (firstChar == 'u'):
                # Prompt
                secondPart = splitLine[1].strip("()")
                if ('_' in secondPart):
                    self.withUnderscore.append(secondPart)
                thirdPart = splitLine[2]
                if (len(firstPart) > 1):
                    # un
                    curNum = ord(firstPart[1]) - 48
                    if (lastNum >= curNum):
                        curSeq = [self.root[curSeqKey[0]]]
                        for i in range(1, curNum):
                            curSeq = [curSeq[0][1][curSeqKey[i]]]
                    if (thirdPart[0] == '['):
                        curSeq[0][1][secondPart] = [self.strList2List(thirdPart), {}]
                    else:
                        curSeq[0][1][secondPart] = [thirdPart, {}]
                    curSeq = [curSeq[0][1][secondPart]]
                    curSeqKey.append(secondPart)
                    lastNum = curNum
                else:
                    # u
                    # first key
                    curSeqKey = []
                    if (thirdPart[0] == '['):
                        self.root[secondPart] = [self.strList2List(thirdPart), {}]
                    else:
                        self.root[secondPart] = [thirdPart, {}]
                    curSeq = [self.root[secondPart]]
                    curSeqKey.append(secondPart)            
        return

    def strList2List(self, strList):
        newList = []
        newStrList = strList.strip("[]")
        tempStr = ""
        openQuote = False
        for index in range(len(newStrList)):
            secondChars = newStrList[index]
            if (secondChars != ' ' or openQuote):
                tempStr += secondChars
            if (secondChars == '\"'):
                openQuote = not openQuote
            if ((secondChars == ' ' and not openQuote) or index == len(newStrList)-1):
                if (not newList):
                    newList = [tempStr]
                else:
                    newList.append(tempStr)
                tempStr = ""
        return newList

    def respond(self):
        end = False
        curConv = [self.root]
        while not end:
            userInput = input("Input: ").strip().lower()
            userInput = re.sub(' {2,}', ' ', userInput)
            validPrompt = curConv[0].keys()                      
            closestMatch = list(validPrompt)
            for matchInd in range(1, len(userInput) + 1):
                closestMatch = [k for k in closestMatch if k.startswith(userInput[0:matchInd])]
                # print(userInput[0:matchInd])
                # print(closestMatch)
                if (len(closestMatch) == 1):
                    # print(closestMatch[0])
                    closestMatch = closestMatch[0]
                    if not ('_' in closestMatch):
                        closestMatch = []
                    break
                    
            # if closestMatch:
            #     matchFound = True
            #     for matchInd in range(len(userInput)):
            #         matchFound = not(closestMatch[matchInd] == userInput[matchInd])
            #         if matchFound:
            #             break






            
                        
                
                
            if (userInput in ["bye", "goodbye", "good bye"]):
                end = True
            elif closestMatch:
                splitMatch = closestMatch.split()
                splitUser = userInput.split()
                storeVar = ""
                # Fast Check if Valid User Input
                if (len(splitMatch) <= len(splitUser)):
                    for index in range(len(splitMatch)):
                        if (splitMatch[index] == '_'):
                            storeVar = splitUser[index]
                    responseMessage = curConv[0][closestMatch][0]
                    splitResponseMessage = responseMessage.split()
                    for keyName in splitResponseMessage:
                        if (keyName[0] == '$'):
                            self.userVariable[keyName] = storeVar
                            responseMessage = responseMessage.replace(keyName, self.userVariable[keyName])
                            curConv = [curConv[0][closestMatch][1]]
                            if (len(curConv[0]) == 0):
                                curConv = [self.root]
                            print("Chat Bot: ", end='')
                            print(responseMessage)
                            talkBack(responseMessage)
            elif userInput in validPrompt:
                responseMessage = curConv[0][userInput][0]
                if responseMessage[0] == '~':
                    # tilde
                    responseMessage = self.customVariable[responseMessage]
                if (type(responseMessage) == list):
                    responseMessage = random.choice(responseMessage)
                if ('$' in responseMessage):
                    splitResponseMessage = responseMessage.split()
                    for keyName in splitResponseMessage:
                        if (keyName[0] == '$'):
                            if (keyName in self.userVariable.keys()):
                                responseMessage = responseMessage.replace(keyName, self.userVariable[keyName])
                            else:
                                responseMessage = "I don't know"
                                print("Chat Bot: ", end='')
                                print(responseMessage)
                                talkBack(responseMessage)
                    

                curConv = [curConv[0][userInput][1]]
                if (len(curConv[0]) == 0):
                    curConv = [self.root]
                print("Chat Bot: ", end='')
                print(responseMessage)
                talkBack(responseMessage)
            
            
            else:
                tildeKey = ""
                for key in curConv[0].keys():
                    if ('~' in key):
                        # Variable found
                        tildeKey = key
                        
                if (tildeKey != "") and (userInput in self.customVariable[tildeKey]):
                    responseMessage = curConv[0][tildeKey][0]
                    if (type(responseMessage) == list):
                        responseMessage = random.choice(responseMessage)
                    curConv = [curConv[0][tildeKey][1]]
                    if (len(curConv[0]) == 0):
                        curConv = [self.root]
                    print("Chat Bot: ", end='')
                    print(responseMessage)
                    talkBack(responseMessage)
                else:
                    responseMessage = "I don't understand"
                    print("Chat Bot: ", end='')
                    print(responseMessage)
                    talkBack(responseMessage)

    
        
        

def main():
   Dialog_Engine('liveDemoFile.txt')

main()
