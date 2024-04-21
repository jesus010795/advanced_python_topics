
fruits = ['manzana','melon','pera','platano']


enum_fruits = enumerate(fruits)

for index, fruit in enum_fruits:
    print(f"indice {index}, fruta {fruit}")

print(list(enum_fruits))
