a=[1,3,5,2,2]
b=sum(a)
left = 0
for i in range(len(a)):
  b=b-a[i]
  if left == b:
    print(i+1)
  left = left+a[i]