def maior(coleção):
    maior_i = coleção[0]
    for item in coleção:
         if item > maior_i:
             maior_i = item
    return maior_i

print(maior([1, 2, 3, 4, 5, 777, 7]))
