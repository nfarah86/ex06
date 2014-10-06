import sys

def sortedRatings(scoreFile):

    restaurantScores = {}

    for line in scoreFile:
        noSpaces = line.strip()
        key, value = noSpaces.split(':')
        restaurantScores[key] = int(value)
    alphaKeys = sorted(restaurantScores.keys())

    for item in alphaKeys:
        print "Restaurant %s is rated at %r." % (item, restaurantScores[item])

def main():
    filename = open(sys.argv[1])
    sortedRatings(filename)

if __name__ == "__main__":
    main()