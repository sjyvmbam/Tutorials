import sys

a=int(sys.argv[1])
b=int(sys.argv[2])

print("\t", end="")

for i in range(a,b+1):
    print (i, end="\t")
print()

for i in range(a,b+1):
    print(i, end="\t")

    for k in range(a,b+1):
        print(i*k, end="\t")
    print()





