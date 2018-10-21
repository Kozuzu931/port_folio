# ハッシュテーブルを作ってみる

# ハッシュテーブル用のクラス
class MyDictUsingHashTable:
  def __init__(self):  # コンストラクタ
    self.count = 0
    self.size = 256
    self.mask = 255
    self.table = [None]*self.size

  # キーの削除
  def pop(self, key):
    t = self.table
    v = None
    i = (hash(key) & self.mask)
    if t[i].key == key:
      v = t[i].value
      t[i] = None
    else:
      raise # ハッシュ衝突が起きたら例外を発生させる
    self.count -= 1
    return v

  # ハッシュテーブルの現在の様子を文字列化。
  #  __str__という特別な関数を定義しておくと、
  # 当該クラスのインスタンスx について str(x) としたときに動作を定義できる。
  # 今の場合はハッシュテーブルの中の様子が表示される。
  def __str__(self):
    s = '< '
    for i in range(0,self.size):
      if self.table[i] != None:
        s += str(self.table[i])+' '
    s += '>'
    return s

  # キーと値の登録
  def setitem(self, k, v):
    i = hash(k) & self.mask # kのハッシュ値と self.mask を &演算 する
    if self.table[i] == None:
      # 計算したテーブルの行が空なのでキーと値を登録
      self.table[i] = _Entry(k,v)
    else:
      # 空でない場合
      if t[i].key == key:
        # 同じキーなので値を更新
        self.table[i].value = v
      else:
        raise # ハッシュ衝突が起きたら例外を発生させる
    self.count += 1


#ハッシュテーブルに登録される内部ノード用のクラス
class _Entry:
  def __init__(self, k, v):
    self.key = k
    self.value = v
  def __str__(self):
    return str(self.key)+'-->'+str(self.value)


# 以下はテストコード
x = MyDictUsingHashTable()
print('初期状態', x)
x.setitem('apple', 'リンゴ')
print('apple 追加', x)
x.setitem('banana', 'ばなな')
print('banana追加', x)
x.pop('banana')
print('banana削除', x)
x.pop('apple')
print('apple 削除', x)
