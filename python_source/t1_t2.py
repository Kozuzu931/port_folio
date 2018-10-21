import re
def to_minite(m):
    n=re.search(r"(\d{1,2}):(\d{1,2})",m)
    hour=int(n.group(1))*60
    minitue=int(n.group(2))
    return hour+minitue
def time_diff(t1,t2):
    m1=to_minite(t1)
    m2=to_minite(t2)
    return abs(m1-m2)


import re
m="AM10:50"
n=re.search(r"(\d{1,2}):(\d{1,2})",m)
a=re.search(r"AM|PM|am|pm",m)
if a.group=="PM" or "pm":
  print("a")
elif a==None:
  print("b")
