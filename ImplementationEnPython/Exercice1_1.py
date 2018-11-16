bool = True
while bool:
    sexe = input("le Sexe : ")
    lage = int(input("l'age : "))
    if sexe == "homme" and lage >= 20 :
        print("vous devez payer l'impot ")
    elif sexe == "femme" and lage >= 18 and lage <= 35 :
        print("vous devez payer l'mpot")
    else :
        print("ne payee pas l'impot")
    
