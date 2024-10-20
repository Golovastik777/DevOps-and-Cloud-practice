f = open('A.txt')
a = [int(x) for x in f.readlines().split()]
print(a)