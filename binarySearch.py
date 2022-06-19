import argparse
import sys


testList = []
for i in range(100):
    testList.append(i)

testStartingIndex = 0
testEndingIndex = len(testList)-1
target = 99


def binarySearch(aList, startingIndex, endingIndex, target, log=""):
    middleElementIndex = (startingIndex + endingIndex) // 2

    if log != "":
        print(f"Target: {target}. Middle Element: {aList[middleElementIndex]}")
        print(aList[startingIndex:endingIndex + 1],"\n")
    
    if startingIndex > endingIndex:
        print("This number is not in the list.")
        return False

    if target == aList[middleElementIndex]:
        print(f"Number found in position {middleElementIndex} of the list.")
        return True

    if  target < aList[middleElementIndex]:
        binarySearch(aList, startingIndex, middleElementIndex - 1, target)
    else:
        binarySearch(aList, middleElementIndex + 1, endingIndex, target)


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('log')
    args = parser.parse_args(argv)

    if args.log == '':
        binarySearch(testList, testStartingIndex, testEndingIndex, target)
    else:
        binarySearch(testList, testStartingIndex, testEndingIndex, target, args.log)


if __name__ == '__main__':
    main()
