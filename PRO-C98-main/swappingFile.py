def SwapFileData():
    firstFile     =   input("Enter your file name :  ")
    secondFile    =   input("Enter your file name :  ")
    with open(firstFile,'r') as data_A:
        data_a    =   data_A.read()

    with open(secondFile, 'r') as data_B:
        data_b = data_B.read()

    with open(firstFile, 'w') as data_A:
        data_A.write(data_b)

    with open(secondFile, 'w') as data_B:
        data_B.write(data_a)

SwapFileData()