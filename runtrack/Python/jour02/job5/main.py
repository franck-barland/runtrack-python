#job5

def operationWth2Terms():
    #Declar./type/init. variables
    num1=float()
    op=str("")
    num2=float()
    questionForNum1=str("Veuillez entrer le premier terme SVP: ")
    questionForNum2=str("Veuillez entrer le deuxième terme SVP: ")
    rslt=float()
    #entries and exception manag. of operator & numeric datas entries
    num1,questionForNum1,op,num2,questionForNum2 = doAllEntriesWithExceptions(num1,questionForNum1,op,num2,questionForNum2)
    #execution
    num1,op,num2,rslt = doOperation(num1,op,num2,rslt)
    #final imp.
    print("Le résultat est : ", rslt)

#Entries for all the datas
def doAllEntriesWithExceptions(num1,questionForNum1,op,num2,questionForNum2):
    # 1st entry
    num1=exceptionsNumEntry(num1,questionForNum1)
    # operator
    op=exceptionsOperEntry(op)
    # 2nd entry
    num2=exceptionsNumEntry(num2,questionForNum2)
    return (num1,questionForNum1,op,num2,questionForNum2)

def exceptionsOperEntry(op):
    op=input("Veuillez entrer votre opérateur (+ - * / %) : ")
    if op == "+" or op == "-"  or op == "*" or op == "/" or op == "%":
        print("Vous avez donc choisi: ",op)
        return op
    else :
        print("votre opérateur n'est pas reconnu... Veuillez recommencer, SVP: ")
        exceptionsOperEntry(op)

def exceptionsNumEntry(x,question):
    while True:
        try:
            x=float(input(question))
            break
        except ValueError:
            print("Attention, il faut entrer une valeur "+ 
            "numérique, SVP!!! Essayez encore: ")
    return x

#execution of operation
def doOperation(num1,op,num2,rslt):
    if op == "+":
        rslt = num1 + num2
    elif op == "-":
        rslt= num1 - num2
    elif op == "*":
        rslt= num1 * num2
    elif op == "/":
        rslt= num1 / num2
    elif op == "%":
        rslt = num1 % num2
    return (num1,op,num2,rslt)

#exec.
operationWth2Terms()