from numpy import linspace, arange
import matplotlib.pyplot as plt

def getMaxNumber(array):
    length = len(array)
    maxNumber = array[0]

    for i in range(length):
        number = array[i]
        if number > maxNumber:
            maxNumber = number

    return maxNumber

def sortDict(dictionary):
    sortedDict = {}
    keys = dictionary.keys()
    keys = sorted(keys)
    for key in keys:
        sortedDict[key] = dictionary[key]
    return sortedDict

text = input('Введите любой текст >> ')
lettersToSave = list('qwertyuiopasdfghjklzxcvbnm')
letters = {}

for i in range(len(text)):
    symbol = text[i].lower()

    if not symbol in lettersToSave:
        continue
    
    if not symbol in letters:
        letters[symbol] = 1
        continue

    letters[symbol] += 1

letters = sortDict(letters)
values = list(letters.values())
lettersCount = len(values)
maxCounted = getMaxNumber(values)

plt.bar(range(lettersCount), values)
plt.ylabel('Частота')
plt.title('Частота появления букв')
plt.xticks(range(lettersCount), list(letters.keys()))
plt.yticks(range(0, maxCounted + 1))

plt.savefig('graph_2.png', dpi=200)
plt.show()