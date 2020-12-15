import jellyfish
import time

file = open("misspell.txt", 'r')
mis = file.readlines()
file.close()

file = open("correct.txt", 'r')
cor = file.readlines()
file.close()

file = open("dict.txt", 'r')
dic = file.readlines()
file.close()

num = 0
correctnum = 0

writeTXT = open("Metaphone.txt", "w")

dictionary = []
for line in dic:
    temp = line.strip()
    dictionary.append(temp)

correct = []
for line in cor:
    temp = line.strip()
    correct.append(temp)

misspell = []
for line in mis:
    temp = line.strip()
    misspell.append(temp)

time_start = time.time()

metacodes = []
for dicWord in dictionary:
    metacode = jellyfish.metaphone(dicWord)
    metacodes.append(metacode)

for line in range(0, len(misspell)):
    current = misspell[line]
    prediction = []
    result = []
    metacode = jellyfish.metaphone(current)

    for meta in range(0,len(metacodes)):
        if metacode == metacodes[meta]:
            prediction.append(dictionary[meta])
            num += 1

    if correct[line] in prediction:
        correctnum += 1
        result.append("T")
    else:
        result.append("F")

    writeTXT.write(current + ',' + metacode + ',' + str(prediction) + ',' + str(result) + '\n')

time_end = time.time()

runtime = time_end - time_start

pricision = (float(correctnum) / float(num)) * 100
recall = (float(correctnum) / float(10322)) * 100

print(correctnum, num, pricision, recall)
print(str(runtime))
writeTXT.write("correctnum = " + str(correctnum) + '\n' + "totalnum = " + str(num) + '\n' + "pricision = " + str(
    pricision) + '\n' + "recall = " + str(recall) + "\n" + "runtime = " + str(runtime))

writeTXT.close()
