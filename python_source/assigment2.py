a  = [[1,2],
      [3,4],
      [5,6]]

b = [[2,4],
     [4,4],
     [6,3]]
result = []
for i in range(len(a)):
    for j in range(len(a[:][i])):
             pre = a[i][j] + b[i][j]
             result.append(pre)
final = [result[i: i + 2] for i in range(0, len(result),2)]
print(final)




    