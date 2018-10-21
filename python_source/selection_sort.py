a=[5, 2, 3, 1, 4]
print("ソート前:",a)
for i in range(0,len(a)-1):
  min=a[i]
  minpos=i
  for j in range(i+1,len(a)):
    if a[j] < min:
      min=a[j]
      minpos=j
  if i != minpos:
    t=a[i]
    a[i]=min
    a[minpos]=t
  print(a)
print("ソート後: ",a)
