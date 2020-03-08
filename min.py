import sys

def avg(zahlen):
  return (sum(zahlen)/len(zahlen))

def min(zahlen):
  min = zahlen[0]
  for i in zahlen:
    if i < min: min = i
  return min

def max(zahlen):
  max = zahlen[0]
  for i in zahlen:
    if i > max: max = i
  return max

z = []
for zeile in sys.stdin:
  z += [float(zeile)]

print("Durchschnitt:",avg(z))
print("Minimum:",min(z))
print("Maximum:",max(z))


'''a=[3,10,0,2,5]
min=0
b=[]
max=0
for i in range(len(a)):
    for j in range(len(a)-1,-1,-1):
        if a[i]<a[j]:
            b+=a[i]

            print(b)

        elif a[j]<a[i]:
            min=a[j]



        j-=1
    i+=1'''