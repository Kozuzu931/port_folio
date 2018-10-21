#
# ノードとリンクのクラス定義 (ノードを先に生成しないとまずいつくりなので注意)
#

import math
import re
from project import project

# 以下の2関数は http://qiita.com/s-wakaba/items/e12f2a575b6885579df7 を改変して利用
def latlng_to_xyz(lat, lng):
    rlat, rlng = math.radians(lat), math.radians(lng)
    coslat = math.cos(rlat)
    return coslat*math.cos(rlng), coslat*math.sin(rlng), math.sin(rlat)

def dist_on_sphere(pos0, pos1, radius=6378.137):
    xyz0, xyz1 = latlng_to_xyz(*pos0), latlng_to_xyz(*pos1)
    return math.acos(sum(x * y for x, y in zip(xyz0, xyz1)))*radius


class Node:
  all_nodes = {}
  hms_regexp = re.compile(r'([0-9]+)\.([0-9]+)\.([0-9.]+)')

  @classmethod
  def find(cls, id):
    return cls.all_nodes[id]

  @classmethod
  def get_all_nodes(cls):
    return cls.all_nodes.values()

  @classmethod
  def from_feature(cls, feat):
    if project == 'ikebukuro':
      prop = feat['properties']
      node_id = prop['ノードID']
      match = cls.hms_regexp.fullmatch(prop['緯度'])
      lat = float(match.group(1)) + float(match.group(2)) / 60.0 + float(match.group(3)) / 3600.0
      match = cls.hms_regexp.fullmatch(prop['経度'])
      lng = float(match.group(1)) + float(match.group(2)) / 60.0 + float(match.group(3)) / 3600.0
      cls(node_id, (lat, lng))
    else: # elif project == 'akabane':
      prop = feat
      node_id = feat['properties']['id']
      coord = feat['geometry']['coordinates']
      print(node_id, coord[0], coord[1])
      cls(node_id, (coord[0], coord[1]))

  def __init__(self, node_id, latlng):
    self.id = node_id
    self.latlng = latlng
    self.links = []
    self.all_nodes[self.id] = self
    self.distance = float('inf') # 最短経路計算用(dijkstra.pyで使う)
    self.route = None # 最短経路計算用(dijkstra.pyで使う)

  # これはLinkクラス専用
  def add_link(self, link):
    self.links.append(link)

  def __str__(self):
    return str(self.id)


class Link:
  all_links = {}

  @classmethod
  def find(cls, id):
    return cls.all_links[id]

  @classmethod
  def from_feature(cls, feat):
    if project == 'ikebukuro':
      prop = feat['properties']
      link_id = prop['リンクID']
      node1_id = prop['起点ノード']
      node2_id = prop['終点ノード']
      cls(link_id, node1_id, node2_id)
    else: # elif project == 'akabane':
      prop = feat['properties']
      #print(prop)
      cls(prop['id'], prop['start'], prop['end'])

  def __init__(self, link_id, node1_id, node2_id, len=None):
    assert node1_id != node2_id
    self.id = link_id
    self.nodes = (Node.find(node1_id), Node.find(node2_id))
    if len == None:
      self.length = dist_on_sphere(self.nodes[0].latlng, self.nodes[1].latlng)
    else:
      self.length = len
    self.all_links[self.id] = self
    # Nodeから参照できるようにしておく
    for n in self.nodes:
      n.add_link(self)

  # 引数 node と反対側のノードを返す (nodeが始点なら終点, 終点なら始点を返す)
  def opposite(self, node):
    for n in self.nodes:
      if n.id != node.id:
        return n

  def __repr__(self):
    return str(self.nodes[0])+'-'+str(self.nodes[1])

