dictFile = open('enable1.txt', 'r')

letters = input("> ")
possibleWordsList = [word for word in dictFile.read().split() if set(word).issubset(set(letters))]
possibleWordsLists = sorted(possibleWordsList, key=len)
print(possibleWordsList[-1])