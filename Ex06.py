import sys

def setupDictionary(scoreFile):

    restaurantScores = {}

    for line in scoreFile:
        noSpaces = line.strip()
        key, value = noSpaces.split(':')
        restaurantScores[key] = int(value)
    print restaurantScores
    return restaurantScores

def sortedName(dictionary):
    alphaKeys = sorted(restaurantScores.keys())

    for item in alphaKeys:
        print "Restaurant %s is rated at %r." % (item, restaurantScores[item])

def sortedRatings(dictionary):
    pass

def main():
    fileObject = open(sys.argv[1])
    restaurantDictionary = setupDictionary(fileObject)

if __name__ == "__main__":
    main()