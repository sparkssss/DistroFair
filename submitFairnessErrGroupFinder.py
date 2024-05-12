totCount = {'wheel': 7435, 'car': 4765, 'person': 4580, 'bicycle': 1425, 'traffic light': 760, 'license plate': 320, 'bus': 225, 'truck': 110, 'train': 105, 'motorcycle': 75, 'shoe': 40, 'bench': 15, 'airplane': 10, 'road sign': 5, 'door': 5}

err1Count = {'wheel': 709, 'person': 106, 'car': 96, 'license plate': 84, 'bicycle': 44, 'traffic light': 14, 'bus': 14, 'shoe': 2, 'motorcycle': 2, 'truck': 1}

err2Count = {'wheel': 190, 'person': 121, 'car': 80, 'bicycle': 36, 'bus': 21, 'airplane': 18, 'truck': 9, 'train': 7, 'traffic light': 6, 'horse': 3, 'license plate': 3, 'bird': 2, 'dog': 2, 'helicopter': 2, 'bench': 1, 'motorcycle': 1, 'helmet': 1}

print("Old Length")
print(len(totCount))

for elem in list(totCount):
    
    curCount = totCount[elem]
    
    if curCount<10:
        
        totCount.pop(elem)

print("New Length")
print(len(totCount))

err1PerCount = {}
err2PerCount = {}

for elem in totCount:
    
    if elem in err1Count:
    
        perError = err1Count[elem]/totCount[elem]
        
        err1PerCount[elem] = perError
    
    if elem in err2Count:
        
        perError = err2Count[elem]/totCount[elem]
        
        err2PerCount[elem] = perError

from collections import Counter

err1PerCount = Counter(err1PerCount)
err2PerCount = Counter(err2PerCount)

# print(err1PerCount)
# print(err2PerCount)

err1CountOver10 = {}
err2CountOver10 = {}

# print(len(err1PerCount))

intCalcList = err1PerCount.values()
err1Avg = sum(intCalcList)/len(intCalcList)

intCalcList = err2PerCount.values()
err2Avg = sum(intCalcList)/len(intCalcList)

print(err1Avg)
print(err1PerCount)

print(err2Avg)
print(err2PerCount)

for elem in err1PerCount.most_common():
    
    val = elem[1]
    
    if val>err1Avg:
        
        elem = elem[0]
        
        curCount = err1Count[elem]
        
        err1CountOver10[elem] = curCount

for elem in err2PerCount.most_common():
    
    val = elem[1]
    
    if val>err2Avg:
        
        elem = elem[0]
        
        curCount = err2Count[elem]
        
        err2CountOver10[elem] = curCount

#print(len(err1CountOver10))
print(err1CountOver10)
print(err1CountOver10.keys())

#print(len(err2CountOver10))
print(err2CountOver10)
print(err2CountOver10.keys())

print("New Length")
print(len(totCount))

print("Type 1")
print(len(err1CountOver10.keys()))

print("Type 2")
print(len(err2CountOver10.keys()))
