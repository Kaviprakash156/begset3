n=int(input("enter the number of elements:\n"))
l=[]
for i in range(0,n):
  i=int(input("enter the element:\n"))
  l.append(i)
  print (l)
l.sort()
print (l)
k = len(l)
if (k % 2 == 0):
    median = (l[(k)//2] + l[(k)//2-1]) / 2
else:
    median = l[(k-1)//2]
print (median)
