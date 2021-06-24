nombres = [1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 7, 8, 9, 10]
     
nombres_sans_duplicats = []
     
for i in nombres:
        if i not in nombres_sans_duplicats:
            nombres_sans_duplicats.append(i)
     
print(nombres_sans_duplicats)