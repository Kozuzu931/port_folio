def pyramid(n):
  count=1
  x=0
  while count <= n:
    print(" "*(n-x),"##"*count," "*(n-x))
    count+=1
    x+=1
