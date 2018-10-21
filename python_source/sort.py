a=[10,5,2,3,1,4,8,9,6,7,11]
print("ソート前：",a)
c=0
for i in range(0,len(a)-1):
    min=a[i]
    minpos=i
    for j in range(i+1,len(a)):
        c+=1
        print(c,"回目の比較です")
        if a[j]<min:
            min=a[j]
            minpos=j
            if i != minpos:
                t=a[i]
                a[i]=min
                a[minpos]=t

    print("ソート後：",a)
print(c,"回の比較でした")
