#job5 err => PGCD + primary number


def resaerchPrimaryNumber():
    #declar/typ/init
    number=int()
    testNumber=float()
    list=[]
    

    #loopLenghDefinition
    number=int(input("veuillez entrer votre nombre :"))

    for i in range(number-1):
       for j in range(i-1):
            if float((i+1)%(j+1)) == 0:
                    list.append(i+1)
                    print(i+1)

'''    for i in range(number-1):
         if 
    '''
resaerchPrimaryNumber()
