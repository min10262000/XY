
import random
import time

filePath = "rank.txt"
maxRankUser = 5
numberProblem = 10

def numberToOperator(number):
    if number == 0:
        return "+"
    elif number == 1:
        return "-"
    elif number == 2:
        return "*"
    elif number == 3:
        return "/"
    return ""


def getAnswer(number1,operator,number2): 
    if operator == 0:
        return number1+number2
    elif operator == 1:
        return number1-number2
    elif operator == 2:
        return number1*number2
    elif operator == 3:
        return number1/number2

    return 0

def saveRank(name,time): 
    f = open(filePath, 'a')
    f.write(name + ",")
    #f.write(",")
    f.write(str(time) + "\n")
    f.close()

def generateProblem():
    randomNumber1 = random.randrange(1, 10)
    randomOperator = random.randrange(0, 4)    
    randomNumber2 = random.randrange(1, 10)

    
    numberAnswer = getAnswer(randomNumber1,randomOperator,randomNumber2)

    if randomOperator%2 == 1:  
        numberAnswer = getAnswer(randomNumber1,randomOperator-1,randomNumber2)        
        temp = numberAnswer
        numberAnswer = randomNumber1
        randomNumber1 = temp

    return [randomNumber1,randomOperator,randomNumber2,numberAnswer]

def printProblem(problem):
    print str(problem[0]) + numberToOperator(problem[1]) +  str(problem[2]) + "=?"

def startGame():
    start_time = time.time()  
    panaltytime = 0
    counter = 0
    for i in range(0, numberProblem): 
        #print ("" + str(i) + " " + str(random.randrange(0,10)))
        problem = generateProblem()
        printProblem(problem)
        
        userAnswer = raw_input("? ")
        if int(userAnswer) == problem[3]:
            counter += 1 #counter+1
            print "Correct"           
        else:
            panaltyime += 10.0
            print "Wrong"


    end_time = time.time()
    playTime = round(end_time - start_time,2) + panaltyTime
    print playTime

    return playTime

def readRecodes():
    f = open(filePath, 'r')
    lines = f.readlines()
    f.close()

    records = []
    for line in lines:    
        #print(line)
        splitedLine = line.strip().split(',')
        #print splitedLine[0]
        #print splitedLine[1]
        recordName = splitedLine[0]
        recordTime = splitedLine[1]
        records.append(splitedLine)
    #print records

    return records

def findRecodePosition(records,playTime,counter):
    if conter != numberProblem:
        return maxRankUser

    newRanking = maxRankUser # 0 1 2 3 4 [5]    
    for i in range(0,maxRankUser): #iterator 
        if playTime < float(records[i][1]): # i  0 1 2 3 4
            #print str(playTime) + " am faster then " + str(i) + ", " + records[i][1]
            #stop
            newRanking = i
            return i
        #else: 
            #print str(playTime) + " am slower then " + str(i) + ", " + records[i][1]
    #print "new ranking is " + str(i+1)
    return i+1


def addNewRecode(newRanking,names,playTime):
    records.insert(newRanking,[names,str(playTime)]) #[name,str]
    return records[0:5]


def saveRecords(records):
    f = open(filePath,'w')
    f.close()

    for i in range(0,maxRankUser):
        saveRank(records[i][0],records[i][1])





def playGame():
    playTime, counter = startGame()
    
    records = readRecodes()
    newRanking = findRecodePosition(records, playTime, counter)
    if newRanking < 5:
        names = raw_input("Name: ")
        print names
        records = addNewRecode(newRanking, names, playTime)
        saveRecords(records)

def viewRank():
    records = readRecodes()
    print ""
    print "name  time"
    print "----------"
    for record in records:
        print record[0] + "   " +record[1]

def executeGame():
    menu = raw_input("1. game start\n2. view rank\n3. game end\nselect menu: ")
    if menu == '1':
        doGame()
    elif menu == '2':
        viewRank()

executeGame()

    #[1,2,3,4] append(4)
    #[4,1,2,3] insert(4)
  #       0     1 
  # 0 [['aaa', '1'], 
  # 1 ['bbb', '2'], 
  # 2 ['ccc', '3'], 
  # 3 ['ddd', '40'], 
  # 4 ['eee', '45']]
  # records[0][1] => 1

#records
#   0     1     2     3     4  
#['15', '20', '30', '40', '45']





#str()  --> 'asdjkl'
#int()   -->integer  1 2 3 4 5
#float()  --> real number 12.21313 -454.325345

#['1', '2', '3', '4.13599991798', '40']
#aaa  bbb  ccc    new user        ddd

    #1 aaa
    #2 15

    #   0     1
    #['nnn',aaa', '15']
    #insert (0,"nnn" )
    #insert (0,"nnn" )
    
    #splitedLine[0] ==> 'aaa'
    #splitedLine[1] ==> '15'





#aaa,15
#bbb,20
#ccc,30
#ddd,40
#eee,45