import weighted_levenshtein
import numpy
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
insert = numpy.ones(128, dtype=numpy.float64) * 1
delete = numpy.ones(128, dtype=numpy.float64) * 1
substitute = numpy.ones((128, 128), dtype=numpy.float64) * 3

writeTXT = open("Weight.txt", "w")

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

for line in range(0, len(misspell)):
    current = misspell[line]
    distance = []
    prediction = []
    result = []

    for dicWord in dictionary:
        dis = weighted_levenshtein.levenshtein(current, dicWord,  insert_costs=insert, delete_costs=delete, substitute_costs=substitute)
        distance.append(dis)

    minimum = min(distance)

    for mini in range(0, len(distance)):
        if distance[mini] == minimum:
            prediction.append(dictionary[mini])
            num += 1

    if correct[line] in prediction:
        correctnum += 1
        result.append("T")
    else:
        result.append("F")

    print(current, prediction, result)

    writeTXT.write(current + ',' + str(prediction) + str(result) + '\n')

time_end = time.time()

runtime = time_end - time_start

pricision = (float(correctnum) / float(num)) * 100
recall = (float(correctnum) / float(10322)) * 100

print(correctnum, num, pricision, recall)
print(str(runtime))
writeTXT.write("correctnum = " + str(correctnum) + '\n' + "totalnum = " + str(num) + '\n' + "pricision = " + str(
    pricision) + '\n' + "recall = " + str(recall) + "\n" + "runtime = " + str(runtime))

writeTXT.close()


