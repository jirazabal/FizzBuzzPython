from SuperFizzBuzz import SuperFizzBuzz

class Test:

    def __init__(self, *args):
        if (len(args) == 2): #start and stop indices
            self.start = args[0] #args[0] is always start
            self.stop = args[1] #args[1] is always stop
        if (len(args) == 1 and type(args[0]) is list):
            self.nonSeqList = args[0] #args[0] is always the list 
        
    
    def testList(self):
        #test custom input of non sequential numbers
        fizzbuzzList = SuperFizzBuzz(self.nonSeqList)
        print("Test: Custom Non-Sequential Numbers")
        print("Default Parameters: 3: 'Fizz', 5: 'Buzz'")
        fizzbuzzList.printSetOfNumbers()
        del self.nonSeqList[:] #make sure to delete contents of list so it's reusable
        print()
        input("Please press Enter to return.")
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
        cInput = 0
        dictLoopIsDone = False
        askForMore = True
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
            while (askForMore):
                cInput = input()
                try:
                    cInput = int(cInput)
                except:
                    print("Please enter a valid number.")
                    continue
                if (cInput == 1 or cInput == 2):
                    askForMore = False
                else:
                    print()
                    print("Please enter a valid number.")
            if (cInput == 1):
                askForMore = True
            if (cInput == 2):
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


