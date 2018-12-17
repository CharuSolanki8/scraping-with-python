#finput = input ("Enter the filename:")
fopen= open ("Your filename.txt")
tree=list() #define a empty list
for piece in fopen:
    x=piece.split()
    for individual in x:
        if individual in tree:
            continue
        else:
            tree.append(individual)
tree.sort()
print (tree)
