from SuperFizzBuzz import SuperFizzBuzz

class Test:

    def __init__(self, *args):
        if (len(args) == 2): #start and stop indices
            self.start = args[0] #args[0] is always start
            self.stop = args[1] #args[1] is always stop
        
    
    def testList(self):

        #test custom input of non sequential numbers
        fizzbuzz1 = SuperFizzBuzz([31, 12, 33, 11, 15])
        print("Test 1: Custom Non-Sequential Numbers")
        fizzbuzz1.printSetOfNumbers()
        print()
        print()

    #part a - Print the numbers from -12 through 145.
    def partATest(self):
        fizzpartA = SuperFizzBuzz(-12, 145)
        print()
        fizzpartA.printSeqRange()
        input("Please press Enter to return.")
        print()

    #part b - For multiples of 3, print “Fizz”
    def partBTest(self):
        fizzPartB = SuperFizzBuzz(self.start, self.stop, {3: 'Fizz'})
        print()
        print("Printing numbers that are multiples of 3 as 'Fizz'...")
        fizzPartB.evaluateCustomInput()
        input("Please press Enter to return.")
        print()
       
    #part c - For Multiples of 7, print “Buzz”
    def partCTest(self):
        fizzPartC = SuperFizzBuzz(self.start, self.stop, {7: 'Buzz'})
        print()
        print("Printing numbers that are multiples of 7 as 'Buzz'...")
        fizzPartC.evaluateCustomInput()
        input("Please press Enter to return.")
        print()
     
     
    #part d - For Multiples of 38, print “Bazz”
    def partDTest(self):
        fizzPartD = SuperFizzBuzz(self.start, self.stop, {38: 'Bazz'})
        print()
        print("Printing numbers that are multiples of 38 as 'Bazz'...")
        fizzPartD.evaluateCustomInput()
        input("Please press Enter to return.")
        print()

    #part e - Print the appropriate combination of tokens for any number that matches more than one of those rules
    def partETest(self):
        dictLoopIsDone = False
        fizzDict = {}
        while (not dictLoopIsDone):
            print()
            print("***********************************************************")
            print("*                                                         *")
            print("*           Please enter the multiple (integer)           *")
            print("*           you would like to evaluate:                   *")
            print("*                                                         *")
            print("***********************************************************")
            print()
            key = int(input())
            print()
            print("***********************************************************")
            print("*                                                         *")
            print("*           Please enter the word you would               *")
            print("*           like to associate with this multiple:         *")
            print("*                                                         *")
            print("***********************************************************")
            print()
            value = input()
            fizzDict[key] = value
            print()
            print("***********************************************************")
            print("*                                                         *")
            print("*     Would you like to add more multiples and words?     *")
            print("*                                                         *")
            print("*    1. Yes                                2. No          *")
            print("*                                                         *")
            print("***********************************************************")
            cInput = int(input())
            if(cInput == 2):
                dictLoopIsDone = True

        print("Printing numbers that are multiples of ", end = "") 
        for k, v in fizzDict.items(): 
            print(k, ",", end="")
        print(" as ", end = "")
        for k, v in fizzDict.items(): 
            print("'" + v +  "'", end="")
        print()
        fizzPartE = SuperFizzBuzz(self.start, self.stop, fizzDict)
        fizzPartE.evaluateCustomInput()
        input("Please press Enter to return.")
        print()


