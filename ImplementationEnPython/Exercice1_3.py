age =  int(input("Entrez l’âge: "))
n_dann =  int(input("Entrez le nombre d'années de permis: "))
n_dacc =  int(input("Entrez le nombre d'accidents: "))
assr = int(input("Entrez le nombre d'années d'assurance: "))
C1 = age >= 25
C2 = n_dann >= 2
C3 = assr > 5
if not C1 and not C2 :
  if n_dacc == 0 :
    situ ="Rouge"
  else:
    situ = "Refusé"
elif not C1 and C2 or C1 and not C2  :
  if n_dacc == 0 :
    situ = "Orange"
  elif n_dacc == 1 :
    situ = "Rouge"
  else:
    situ =  "Refusé"
else:
  if n_dacc ==  0 :
    situ = "Vert"
  elif n_dacc == 1 :
    situ = "Orange"
  elif n_dacc == 2 :
    situ = "Rouge"
  else:
    situ = "Refusé"
if C3 :
  if situ == "Rouge" :
    situ = "Orange"
  elif situ == "Orange" :
    situ = "Vert"
  elif situ == "Vert" :
    situ = "Bleu"

print( "Votre situation : ", situ)