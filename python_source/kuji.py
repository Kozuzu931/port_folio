year=input('生まれた年を入力してください。例：１９６７（年）')
month=input('生まれた月を入力してください。例：０３（月）')
day=input('生まれた日付を入力してください。例：０１（日）')
num=year+month+day
numb=int(num)%6
if numb==0:
    print("大吉")
elif numb==1:
    print("中吉")
elif numb==2:
    print("吉")
elif numb==3:
    print("小吉")
elif numb==4:
    print("凶")
elif numb==5:
    print("大凶")
else:
    print("オンドゥルウラギッタンディスカタチバナザン！！")
#print(int(num),numb)
