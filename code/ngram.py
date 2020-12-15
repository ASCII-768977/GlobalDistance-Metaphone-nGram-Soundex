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

writeTXT = open("2Gram.txt", "w")

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

list3 = [] #所有的ngram统计 也就是b
list4 = [] #所有的ngram列表


for word in dictionary:
    list1 = []
    list2 = []
    for length1 in range(0,len(word)):
        list1.append(word[length1])
    for length2 in range(0,len(list1)):
        if length2 < len(word)-1:
            list2.append(list1[length2] + list1[length2 + 1])
    list3.append(len(list2))
    list4.append(list2)

for line in range(0, len(misspell)):
    current = misspell[line]
    distance = []
    prediction = []
    result = []
    currentlist = [] #分解成小字母
    currentletter = [] #分解成ngram列表
    currentgram = 0 #当前的ngram重置 也就是a

    for length1 in range(0, len(current)):
        currentlist.append(current[length1])
    for length2 in range(0,len(currentlist)):
        if length2 < len(current)-1:
            currentletter.append(currentlist[length2] + currentlist[length2 + 1])
    currentgram = len(currentletter) #a赋值

    for length3 in range(0,len(list4)): #对字典中每个ngram列表查询是否有一样的
        count1 = 0
        count2 = 0
        count = 0#交集c
        for element in currentletter:
            if element in list4[length3]:
                count1+=1
        for element in list4[length3]:
            if element in currentletter:
                count2+=1
        if count1 == count2:
            count = count1
        elif count1>count2:
            count = count2
        else:
            count = count1

        ngram = currentgram + list3[length3] - 2 * count #a+b-2*c

        distance.append(ngram)#算出来的每一个ngram都放进距离列表然后找最小的

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




