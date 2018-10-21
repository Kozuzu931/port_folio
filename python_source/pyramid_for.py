def pyramid(n):
    e=0
    for m in range(0,n):
        print("  "*(n-e),"#"*e,"  "*(n-e))
        e+=1
