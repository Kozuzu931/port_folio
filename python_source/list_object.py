class MylistUsingLinkedList:
    def __init__(self):
        self.link=None
        self.len=0
    def pop(self,pos):
        prev=self
        for i in range(0,pos):
            prev=prev.link
        item=prev.link
        prev.link=item.link
        self.len-=1
        return item

    def insert(self,pos,v):
        prev=self
        for i in range(0,pos):
            prev=prev.link
        new_node=_ListEntry(v)
        new_node.link=prev.link
        prev.link=new_node.value
        self.len+=1
    def __str__(self):
        node=self.link
        ret="HEAD-->"
        while node != None:
            ret+=str(node.value)+"-->"
            note=node.link
        ret+="TAIL"
        return ret
class _ListEnty:
    def __init__(self,v):
        self.link=None
        self.value=v


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
