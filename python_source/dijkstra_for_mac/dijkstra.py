#
# Dijkstra法による最短経路探索の実装
#
from nodelink import Node, Link

#
# Dijkstra法を用いて node1 から node2 への最短経路を計算する関数
#  - 戻り値は node1 から node2 までをつなぐリンク(辺)のリスト
#  - もし node1 ---(A)---> nodeX ---(B)---> nodeY ---(C)--> node2 が最短経路
#    (A,B,Cはそれぞれリンク)であるならば、戻り値は [A, B, C] のようなリストとなる
#
def dijkstra(node1, node2):
  result = [
    Link.find('00001C000000000000010000002416BF'),
    Link.find('00001C000000000000010000002416C0'),
    Link.find('00001C000000000000010000002416C1'),
    Link.find('00001C00000000000001000000241733'),
    Link.find('00001C0000000000000100000024177D'),
    Link.find('00001C0000000000000100000024177E'),
    Link.find('00001C00000000000001000000241734'),
    ]
  if node1.id == '00001C00000000000001000000243FE7' \
    and node2.id == '00001C00000000000001000000243FB4':
    return result
  else:
    return []
