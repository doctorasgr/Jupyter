textA = input("Choose number A: ")
textB = input("Choose number B: ")

numA = int(textA)
numB = int(textB)
def calc(numA,numB):
    if numA > numB:
        print("Number A is bigger than B")
    else:
        print("Number B is bigger than A")
