
def parseMemories():
    retArray = []

    with open("../Save_Files/Memories.txt", 'r') as memoryFile:
        next(memoryFile)
        for line in memoryFile:
            retArray.append(line.split(':')[0])
    
    return retArray