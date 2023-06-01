#essai
'''
Typage de num1 avant condition:  <class 'str'>
Typage de num1 après entrée condition:  <class 'int'>'''    

def essai():
    #declar/typ/init
    entree=""
    conditionEntreeBoucle=0
    num1=int()

    #entrees
    num1=input ("Donnez la valeur svp, sinon la valeur par défaut sera '3'")
    print("Typage de num1 avant condition: ",type(num1))
    if entree==str(num1) :
        conditionEntreeBoucle=1
        (num1)=(3)
    
    num1=int(num1)    
    print("num1=",num1) 

    if conditionEntreeBoucle==1:
        print("Typage de num1 APRES entrée dans condition: ",type(num1))
    else:
        print("Typage de num1 SANS entrée dans condition: ",type(num1))

essai()