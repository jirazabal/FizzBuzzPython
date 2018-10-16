class SuperFizzBuzz:

    def __init__(self, *args):
        #two args passed in, start index and stop index -- respectively 
        if (len(args) == 2 and type(args[0]) is int and type(args[1] is int)):
            self.start = args[0]
            self.stop = args[1]
        #one arg passed in, a list of numbers
        if (len(args) == 1 and type(args[0] is list)):
            self.listNumbers = args[0]
        #dictionary arg passed in with start and stop index
        if (len(args) == 3 and type(args[0] is dict)):
            self.start = args[0]
            self.stop = args[1]
            self.fizzDict = args[2]

    def printSeqRange(self):
        #colors!
        CGREEN  = '\33[32m' #green
        CEND = '\033[0m'

        #iterate from start index to stop index and evaluate each number
        for i in range(self.start, self.stop + 1):
            if (i % 3 == 0 and i % 5 != 0):
                print(CGREEN + "Fizz" + CEND)
                continue
            if (i % 5 == 0 and i % 3 != 0):
                print(CGREEN + "Buzz" + CEND)
                continue
            if (i % 3 == 0 and i % 5 == 0):
                print(CGREEN + "FizzBuzz" + CEND)
            else:
                print(i)

    def printSetOfNumbers(self):
        #colors!
        CRED = '\033[91m' #red
        CEND = '\033[0m'    
        #iterate through list and evaluate each element
        for i in range(len(self.listNumbers)):
            if (self.listNumbers[i] % 3 == 0 and self.listNumbers[i] % 5 != 0):
                print(CRED + "Fizz" + CEND)
                continue
            if (self.listNumbers[i] % 5 == 0 and self.listNumbers[i] % 3 != 0):
                print(CRED + "Buzz" + CEND)
                continue
            if (self.listNumbers[i] % 3 == 0 and self.listNumbers[i] % 5 == 0):
                print(CRED + "FizzBuzz" + CEND)
            else:
                print(self.listNumbers[i])

    
    def evaluateCustomInput(self):

        #for pretty colors!
        CBLUE = '\33[34m' #blue
        CEND = '\033[0m'
        #flag to not print out number multiple times
        containsWord = False

        for i in range(self.start, self.stop + 1):
            for key, value in self.fizzDict.items():
                if (i % key == 0):
                    print(CBLUE + value + CEND, end ="")
                    containsWord = True
                    continue
            if (not containsWord):
                print(i, end = "")
            containsWord = False
            print()
