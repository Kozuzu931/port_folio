#
# プログラム本体(Webサーバー)
#

import json
import time
from bottle import debug, get, post, request, response, run, static_file
from dijkstra import dijkstra
from nodelink import Node, Link
from project import project

def init():
  with open('./static/data/node_' + project + '.geojson', encoding='utf-8') as f:
    global nodes_geojson
    nodes_geojson = json.load(f)
  for feat in nodes_geojson['features']:
    try:
      Node.from_feature(feat)
    except:
      print('ignored:', feat)

  with open('./static/data/link_' + project + '.geojson', encoding='utf-8') as f:
    global links_geojson
    links_geojson = json.load(f)
  for feat in links_geojson['features']:
    try:
      Link.from_feature(feat)
    except:
      print('ignored:', feat)

init()
debug(True)

@get('/')
def get_index():
  return static_file('index.html', root="./static")

@get('/css/<path:path>')
def get_css(path):
  return static_file(path, root='./static/css')

@get('/data/link.geojson')
def get_data_link():
  response.content_type = 'application/json'
  return json.dumps(links_geojson)

@get('/data/node.geojson')
def get_data_node():
  response.content_type = 'application/json'
  return json.dumps(nodes_geojson)

@get('/leaflet/<path:path>')
def get_leaflet(path):
  return static_file(path, root='./static/leaflet')

@get('/scripts/<path:path>')
def get_path(path):
  return static_file(path, root='./static/scripts')

@get('/api/config')
def get_config():
  conv = {'akabane': [35.780002, 139.719352], 'ikebukuro': [35.729943, 139.7099687]};
  response.content_type = 'application/json'
  return json.dumps({'project': project, 'center': conv[project]})

@post('/api/dijkstra')
def post_dijkstra():
  response.content_type = 'application/json'
  node1 = Node.find(request.json['start'])
  node2 = Node.find(request.json['end'])
  tm_start = time.perf_counter()
  route = dijkstra(node1, node2)
  print('time: {0:.3f} ms'.format(1000*(time.perf_counter()-tm_start)))
  return json.dumps([ x.id for x in route ])

run(host='127.0.0.1', port='8000', reloader=True)
