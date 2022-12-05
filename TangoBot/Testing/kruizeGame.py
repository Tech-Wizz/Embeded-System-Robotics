import random

def main():

    
    def starting():
        list = [1,3,11,13]
        startingPosition = random.choice(list)
        return(startingPosition)

    def fightORflight():
        list = ["Run","Run","Run","Fight"]
        fight = random.choice(list)
        return(fight)

    def runSucceed():
        list = [1,3,6,7,8,11,12,13]
        randomNode = random.choice(list)
        print(randomNode)
        return(randomNode)

    def randomKey():
        guys = ["NoKey", "NoKey"]
        guys[random.randint(0,1)] = "Key"
        print(guys)
        return guys
        
    hardBad = randomKey()
    robotPosition = starting()
    runSucceed()

    
        
        
    
    

main()
