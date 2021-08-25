def countWords():
    fileName = input('Enter the File Name')
    file = open(fileName, 'r')
    noOfWords = 0
    for line in file:
        words = line.split()
        noOfWords = noOfWords + len(words)
    print('The number of words is ' + str(noOfWords))
countWords()