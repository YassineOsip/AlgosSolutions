scores = input("Entrez les scores des quatre prétendants divisé par ' , '  : ")
nombres = scores.split(",")
a , b , c ,d = nombres

c1 = int(a) > 50
c2 = int(b) > 50 or int(c) > 50 or int(d) > 50
c3 =  a >= b and a >= c and int(a) >= int(d)
c4 = int(a) >= 12,5

if c1 :
  print ("Elu au premier tour")
elif c2 or  not c4:
  print ("Battu, éliminé, sorti !!!")
elif c3 :
  print("Ballotage favorable")
else:
  print("Ballotage défavorable")
