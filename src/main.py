from SuperFizzBuzz import SuperFizzBuzz
from Test import Test

def main():
    #colors!
    CRED = '\033[91m' #red
    CEND = '\033[0m' 
    running = True #flag for main loop
    introDone = False #flag to display intro once
    testCaseScreenShow = True #flag to show test case screen
    testSelection = 0 #selection choice for which test to run
    testCaseRun = 0 #selection for whether or not to run test cases
    nonSeqList = [] #list for custom input


    while (running):
        if (not introDone):
            print("*******************************************************")
            print("*                                                     *")
            print("*" + CRED + "\tWelcome to the FizzBuzz o' Matic 3000!        " + CEND + "*")
            print("*                                                     *")
            print("* This program is simple:                             *")
            print("*                                                     *")
            print("*              Just follow the prompts!               *")
            print("*                                                     *")
            print("*******************************************************")
            print()
            print()
            introDone = True

            print("*******************************************************")
            print("*                                                     *")
            print("*         Would you like to run test cases?           *")
            print("*                                                     *")
            print("*   1. Yes                               2. No        *")
            print("*                                                     *")
            print("*******************************************************")
            print()
            testCaseRun = int(input())

            if (testCaseRun == 1):
                while (testCaseScreenShow):
                    print("*********************************************************")
                    print("*                                                       *")
                    print("*         Which test case would you like to run?        *")
                    print("*                                                       *")
                    print("*  1. Part A - Print the numbers -12 - 145 (inclusive)  *")
                    print("*  2. Part B - For multiples of 3, print 'Fizz'         *")
                    print("*  3. Part C - For multiples of 7, print 'Buzz'         *")
                    print("*  4. Part D - For multiples of 38, print 'Bazz'        *")
                    print("*  5. Part E - Custom input!                            *")
                    print("*                                                       *")
                    print("*                                                       *")
                    print("*                                                       *")
                    print("*  9. Enter non-sequential numbers as a list            *")
                    print("*  0. Exit                                              *")
                    print("*********************************************************")
                    print()
                    testSelection = int(input())

                    if (testSelection == 1):
                        testA = Test()
                        testA.partATest()
                        continue
                    
                    if (testSelection == 2):
                        start = int(input("Please enter a start index: \n"))
                        stop = int(input("Please enter a stop index: \n"))
                        testB = Test(start, stop)
                        testB.partBTest()
                        continue

                    if (testSelection == 3):
                        start = int(input("Please enter a start index: \n"))
                        stop = int(input("Please enter a stop index: \n"))
                        testC = Test(start, stop)
                        testC.partCTest()
                        continue

                    if (testSelection == 4):
                        start = int(input("Please enter a start index: \n"))
                        stop = int(input("Please enter a stop index: \n"))
                        testD = Test(start, stop)
                        testD.partDTest()
                        continue

                    if (testSelection == 5):
                        start = int(input("Please enter a start index: \n"))
                        stop = int(input("Please enter a stop index: \n"))
                        testE = Test(start, stop)
                        testE.partETest()
                        continue

                    if (testSelection == 9):
                        nonSeqNumbers = input("Please enter numbers as comma separated list (e.g. 3, 1, 2)\n")
                        for num in nonSeqNumbers.split(','):
                            nonSeqList.append(int(num))
                        testList = Test(nonSeqList)
                        testList.testList()
                        
                    if (testSelection == 0):
                        testCaseRun = False
                        break

                    else:
                        print("Please enter a valid number...")

        if (testCaseRun == 2):
            print("Exiting program...")
            running = False
        

if __name__ == "__main__":
    main()