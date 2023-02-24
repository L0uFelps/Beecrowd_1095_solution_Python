i = 1
j = 60

contador = 1
print("I={} J={}".format(i,j))
while contador < 60:
    
    i = i + 3
    j = j - 5
    print("I={} J={}".format(i,j))
    contador = contador + 1
    if j == 0:
        break