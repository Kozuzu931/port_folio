from nodelink import Node, Link
from my_dijkstra import dijkstra

s=Node('S', 0)
Node('1', 0)
Node('2', 0)
Node('3', 0)
g=Node('G', 0)

Link('S-1', 'S', '1', len=200)
Link('S-2', 'S', '2', len=340)
Link('1-2', '1', '2', len=140)
Link('1-3', '1', '3', len=240)
Link('2-3', '2', '3', len=150)
Link('3-G', '3', 'G', len=160)

print(dijkstra(s, g))
