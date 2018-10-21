# リンクリストを作ってみる

# リンクリスト本体用のクラス
class MyListUsingLinkedList:
  def __init__(self):  # コンストラクタ
    self.link = None
    self.len = 0

  # pop関数: 位置posのノードを削除してそのオブジェクトを返す
  def pop(self, pos):
    # まず、for i ループでリンクをpos個たどる（現在のノードは prev に格納される）
    prev = self  #リンクリスト本体からスタート
    for i in range(0, pos):
      prev = prev.link  # 現在のノード(prev)を、次のノードへ移動させていく
    item = prev.link  # 現在のノード(prev)は「pos個先のノード」になっている。その次のノードが「削除するノード」(item)
    # ノード「item」の次のノードを、現在のノード(prev)の次のノードにすると、itemがリストから外れたことになる
    prev.link = item.link
    self.len -= 1  # リスト長(リンクリストのノード数)をひとつ減らす
    return item  # 削除したノードのオブジェクトを戻り値として返す

  # insert関数: 位置posに、値vのノードを追加する
  def insert(self, pos, v):
    # まず、for i ループでリンクをpos個たどる（現在のノードは prev に格納される）
    prev = self
    for i in range(0, pos):
      prev = prev.link
    # 現在のノード(prev)は「pos個先のノード」になっている。
    # リストにつなぐ新ノードnew_nodeを作る（コンストラクタ）
    new_node = _ListEntry(v)
    # 新ノードの「次のノード」に、現在のノード(prev)の「次のノード」を代入し、
    # 現在のノード(prev)の「次のノード」を新ノード(new_node)にすると、new_nodeをリストに加えたことになる
    new_node.link =  prev.link # prevの「次ノード」をnew_nodeの「次ノード」に設定する
    prev.link =  new_node# prevの「次ノード」をnew_nodeに設定する
   # リスト長を更新する
    self.len += 1  # リスト長(リンクリストのノード数)をひとつ増やす

  # リンクリストの現在の様子を文字列化。
  #  __str__という特別な関数を定義しておくと、
  # 当該クラスのインスタンスx について str(x) としたときに動作を定義できる。
  # 今の場合はノードのつながりの様子と各ノードの値が表示される。
  def __str__(self):
    node = self.link
    ret = 'HEAD-->'
    while node != None:
      ret += str(node.value) + '-->'
      node = node.link
    ret += 'TAIL'
    return ret

#リンクリストの内部ノード用のクラス
class _ListEntry:
  def __init__(self, v):  # コンストラクタ
    self.link = None
    self.value = v


# 以下はテストコード
x=MyListUsingLinkedList()  # リンクリスト本体のインスタンスをひとつ生成(x)
print('初期状態', str(x))
for i in range(0,4):   # リンクリストの0番目（先頭）に4つのノードを次々と追加（値 i はそれぞれ 0, 1, 2, 3）
  x.insert(0, i)
print('4つ追加', str(x))

x.pop(2)  # 2番目のノードを削除
print('2番削除', str(x))
x.pop(2)  # 2番目のノードを削除
print('2番削除', str(x))
x.pop(0)  # 0番目のノードを削除
print('0番削除', str(x))
x.pop(0)  # 0番目のノードを削除
print('0番削除', str(x))
