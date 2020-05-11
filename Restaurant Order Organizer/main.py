from menu import menu


def checkfile(fName):
    # checks if the first line is correct
    fOpen = open(fName, "r")
    firstLine = fOpen.readline().strip()
    return firstLine == "ROO Version 1 Tropika"


def fileOpen(fName):
    pass


def reader(fName):
    # assume that fName is in correct format
    EOF = ""
    rList = []
    fName.readline()  # get rid of first line
    line = fName.readline()
    # print(line)
    while line != EOF:
        rList.append(line.strip().split(","))
        line = fName.readline()
        # print(line)
    return rList


def splitInfo(nList):
    fDict = dict()
    for order in nList:
        for item in order:
            if item not in fDict:
                fDict[item] = 1
            else:
                fDict[item] += 1
    return fDict


def translator(nDict):
    for i, j in nDict.items():
        print(f"{menu[i]} : {j}")


def main():
    userFile = "text1.txt"  # STREAMLINE DEV
    fileBool = checkfile(userFile)
    if not fileBool:
        print("Incorrect file formatting.")
        exit()
    fOpen = open(userFile, "r")
    infoList = reader(fOpen)
    fDict = splitInfo(infoList)
    final = translator(fDict)
    fOpen.close()


main()
# Next step would be to split the orders from apps and mains.
# number of mains does not matter as it is per box
# but number of apps matter, maybe show total and seperation.
