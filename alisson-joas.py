import random

ben = [3, 3, 2, 4, 2, 3, 5, 2]
weight = [5, 4, 7, 8, 4, 4, 6, 8]

def getCromossomo( size ):
  crom = []
  i = 0
  while i < size:
    genne = random.randint(0, 1)
    crom.append(genne)
    i = i + 1
  return crom

size = 8
crom = getCromossomo( size )

def fitness( crom ):
  i = 0
  beneficio = 0
  peso = 0
  while i < size:
    genne = crom[i]
    if genne == 1:
      beneficio = beneficio + ben[i]
      peso = peso + weight[i]
    i = i + 1
  if peso > 25:
    beneficio = -1
  return beneficio      

beneficio = -1
sizePop = 10

while beneficio < 13:
  crom = getCromossomo( size )
  beneficio = fitness( crom ) 
  print(crom)  
  print(beneficio)
