def SwapFileData():
    file1 = input("Enter file 1's name: ")
    file2 = input("Enter file 2's name: ")
    
    #to choose the files
    with open(file1, 'r') as no1:
        data_no1 = no1.read()
    with open(file2, 'r') as no2:
        data_no2 = no2.read()

    #to swap the files
    with open(file1, 'w') as no1:
        no1.write(data_no2)
    with open(file2, 'w') as no2:
        no2.write(data_no1)
SwapFileData()
