import json
from collections import Counter

'''
orgStreetsAWS = []
orgStreetsMS = []
orgStreetsGCP= []

indCount = -1

with open("Streets_AWS.txt") as fR:
    
    for line in fR:
        
        if indCount==1:
            
            stripLine = line.rstrip('\n')
            
            curDict = json.loads(stripLine)
            
            orgStreetsAWS.append(curDict)
            
        indCount = indCount * (-1)
        
indCount = -1

with open("Streets_MS.txt") as fR:
    
    for line in fR:
        
        if indCount==1:
            
            stripLine = line.rstrip('\n')
            
            curDict = json.loads(stripLine)
            
            orgStreetsMS.append(curDict)
            
        indCount = indCount * (-1)
        
indCount = -1

with open("Streets_GCP.txt") as fR:
    
    for line in fR:
        
        if indCount==1:
            
            stripLine = line.rstrip('\n')
            
            curDict = json.loads(stripLine)
            
            orgStreetsGCP.append(curDict)
            
        indCount = indCount * (-1)
'''



orgCOCOAWS = []
orgCOCOMS = []
orgCOCOGCP= []

indCount = -1

with open("MSCOCO_AWS.txt") as fR:
    
    for line in fR:
        
        if indCount==1:
            
            stripLine = line.rstrip('\n')
            
            curDict = json.loads(stripLine)
            
            orgCOCOAWS.append(curDict)
            
        indCount = indCount * (-1)

indCount = -1

with open("MSCOCO_MS.txt") as fR:
    
    for line in fR:
        
        if indCount==1:
            
            stripLine = line.rstrip('\n')
            
            curDict = json.loads(stripLine)
            
            orgCOCOMS.append(curDict)
            
        indCount = indCount * (-1)

indCount = -1

with open("MSCOCO_GCP.txt") as fR:
    
    for line in fR:
        
        if indCount==1:
            
            stripLine = line.rstrip('\n')
            
            curDict = json.loads(stripLine)
            
            orgCOCOGCP.append(curDict)
            
        indCount = indCount * (-1)



'''
print(len(orgStreetsAWS))
print(len(orgStreetsMS))
print(len(orgStreetsGCP))
'''


print(len(orgCOCOAWS))
print(len(orgCOCOMS))
print(len(orgCOCOGCP))


# classes = ["person", "car", "motorcycle", "truck", "bird", "cat", "dog"]

classes = ["person", "car", "motorcycle", "truck"]

# actFileName = "test"

actFileName = "Iter1RecogMS"

for strItem in range(1):
    
    strItemNum = strItem + 1
    
    print("ITER")
    print(str(strItemNum))
    
    actFileName = "Iter" + str(strItemNum) + "RecogMS"

    fileName = "Insert/MSCOCO/MS/" + actFileName + ".txt"
    
    checkClasses1 = ['van', 'building', 'bus', 'vehicle', 'tree', 'billboard', 'house', 'tower', 'tire', 'cart', 'helmet', 'subway train', 'bench', 'stop sign', 'taxi']
    
    checkClasses2 = ['land vehicle', 'truck', 'cycle', 'parking meter', 'tire', 'electric locomotive', 'wall clock', 'clock']
    
    print("Len 1")
    print(len(checkClasses1))
    print("Len 2")
    print(len(checkClasses2))
    
    
    #orgStreets = orgStreetsAWS
    orgCOCO = orgCOCOMS
    
    firstBool = True
    flipBool = False
    
    curClass = []
    changeInt = 0
    curDictInd = 0
    
    err1ImgCount = 0
    err2ImgCount = 0
    totImgCount = 0
    
    with open(fileName) as fR:
        
        for line in fR:
            
            stripLine = line.rstrip('\n')
            
            if (firstBool):
                
                firstBool = False
            
            if (stripLine.lower() in classes):
                
                curClass = stripLine.lower()
                
                checkClass1Copy = checkClasses1.copy()
                checkClass2Copy = checkClasses2.copy()
                
                if curClass in checkClass1Copy:
                    
                    checkClass1Copy.remove(curClass)
                    
                if curClass in checkClass2Copy:
                    
                    checkClass2Copy.remove(curClass)
                
                totDict = Counter()
                err1Dict = Counter()
                err2Dict = Counter()
                
            if (flipBool):
                
                resDict = json.loads(stripLine)
                
                resCounter = Counter(resDict)
                
                curOrgDict = orgCOCO[curDictInd]
                #curOrgDict = orgStreets[curDictInd]
                
                copyCurOrgDict = curOrgDict.copy()
                
    # Deletion
               
    
    # =============================================================================
    #             if curClass in copyCurOrgDict:
    #                 
    #                 copyCurOrgDict[curClass] = 0
    # =============================================================================
    
    
        
    #  Insertion
    
                if curClass in copyCurOrgDict:
                    
                    copyCurOrgDict[curClass] = copyCurOrgDict[curClass] + changeInt
                else:
                    
                    copyCurOrgDict[curClass] = changeInt
                    
                curExpCounter = Counter(copyCurOrgDict)
                
                err1 = curExpCounter - resCounter
                err2 = resCounter - curExpCounter
                
                totImgCount = totImgCount + 1
                
                for item in checkClass1Copy:
                    
                    if item in err1:
                        
                        err1ImgCount = err1ImgCount + 1
                        
                for item in checkClass2Copy:
                    
                    if item in err2:
                        
                        err2ImgCount = err2ImgCount + 1
                
                totDict = totDict + curExpCounter
                err1Dict = err1Dict + err1
                err2Dict = err2Dict + err2
                
    # Rotate/Delete
    # =============================================================================
    #         if (stripLine.startswith("BremenRotateFinal")):
    #             
    #             
    #             flipBool = True
    #             findInd = stripLine.index('bremen_')
    #             
    #             findString = stripLine[findInd+7:]
    #             
    #             findInd = findString.index('_000019_left')
    #             
    #             findString = findString[:findInd]
    #             
    #             findInt = int(findString)
    #             
    #             curDictInd = findInt
    #             
    #             
    #             
    #             '''
    #             flipBool = True
    #             #findInd = stripLine.index('Out/COCO')
    #             findInd = stripLine.index('Final/COCO')
    #             
    #             #findString = stripLine[findInd+8:]
    #             findString = stripLine[findInd+10:]
    #             
    #             findInd = findString.index('_mask')
    #             
    #             findString = findString[:findInd]
    #             
    #             findInt = int(findString)
    #                           
    #             curDictInd = findInt
    #             '''
    #             
    #         else:
    #             
    #             flipBool = False
    # =============================================================================
    
       
    # Insertion
            if (stripLine.startswith("Clean")):
                
                flipBool = True
                findInd = stripLine.index('Count')
                
                findString = stripLine[findInd+5:-4]
                findInt = int(findString)
                
                changeInt = findInt
                
                '''
                findInd = stripLine.index('bremen_')
    
                findString = stripLine[findInd+7:]
                
                findInd = findString.index('_000019_left')
                
                findString = findString[:findInd]
                
                findInt = int(findString)
                
                curDictInd = findInt
                '''
                
                
                
                findInd = stripLine.index('/COCO')
    
                findString = stripLine[findInd+5:]
                
                findInd = findString.index('Count')
                
                findString = findString[:findInd]
                
                findInt = int(findString)
                
                curDictInd = findInt
                
                
                
            else:
                
                flipBool = False
                
    print("Error 1")
    print(err1ImgCount)
    print("Error 2")
    print(err2ImgCount)
    print("Total")
    print(totImgCount)
