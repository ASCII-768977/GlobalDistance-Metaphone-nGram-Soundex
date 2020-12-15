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

writeTXT = open("soundex.txt", "w")

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

soundexcodes = []
for dicWord in dictionary:
    soundexcode = jellyfish.soundex(dicWord)
    soundexcodes.append(soundexcode)

for line in range(0, len(misspell)):
    current = misspell[line]
    prediction = []
    result = []
    soundexcode = jellyfish.soundex(current)

    for soundex in range(0,len(soundexcodes)):
        if soundexcode == soundexcodes[soundex]:
            prediction.append(dictionary[soundex])
            num += 1

    if correct[line] in prediction:
        correctnum += 1
        result.append("T")
    else:
        result.append("F")

    writeTXT.write(current + ',' + soundexcode + ',' + str(prediction) + ',' + str(result) + '\n')

time_end = time.time()

runtime = time_end - time_start

pricision = (float(correctnum) / float(num)) * 100
recall = (float(correctnum) / float(10322)) * 100

print(correctnum, num, pricision, recall)
print(str(runtime))
writeTXT.write("correctnum = " + str(correctnum) + '\n' + "totalnum = " + str(num) + '\n' + "pricision = " + str(
    pricision) + '\n' + "recall = " + str(recall) + "\n" + "runtime = " + str(runtime))

writeTXT.close()
