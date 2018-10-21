import random
import re
win=0
lose=0
draw=0
c=0
def win_lose(c,d):
    if c==d:
        print("あいこです。")
        global draw
        draw+=1
    elif c==0 and d==1 or c==1 and d==2 or c==2 and d==0:
        print("かちです。")
        global win
        win+=1
    elif d==0 and c==1 or d==1 and c==2 or d==2 and c==0:
        print("負けです")
        global lose
        lose+=1
while c!=5:
    try:
        I=int(input("じゃんけんの手、グー（０）チョキ（１）パー（２）を入力してください"))
        com=random.randint(0,2)
        if I==0 or I==1 or I==2:
             win_lose(I,com)
             c+=1
        elif I != 0:
            print("入力は０、１、２のどれかでお願いします")
            continue
        elif I != 1:
            print("入力は０、１、２のどれかでお願いします")
            continue
        elif I != 2:
            print("入力は０、１、２のどれかでお願いします")
            continue
        else:
            print("入力は０、１、２のどれかでお願いします")
            continue 
    except ValueError:
        print("入力は数字の０、１、２のどれかでお願いします")
        continue
print("５戦中",win,"勝",lose,"敗",draw,"引き分け","  ","勝率は",float(win)/5*100,"%です",sep="")
