import pulp
pr=pulp.LpPproblem("作付け問題",pulp.LpMaximize)
x=pulp.LpVariable("x",lowBound=0)
y=pulp.LpVariable("y",lowBound=0)
z=pulp.LpVariable("z",lowBound=0)
staff=[pulp.LpVariable(staff,lowBound=0)

pr+=x+y+z<=30
pr+=
pr+=0.5*x+0.1*y<=5
pr+=
pr+=100*x+20*y+10*z
pr.solve()
print("最大値は＝x"+str(x.value())+"y="+str(y.value())+"のとき")


"""
>>> import toposort
>>> list(toposort.toposort({
... "D":{"A"},
... "E":{"B","C"},
... "G":{"D","E"},
... "H":{"G","H"}
... }))
[{'B', 'A', 'C'}, {'E', 'D'}, {'G'}, {'H'}]
"""
