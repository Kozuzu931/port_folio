def num_to_str(n):
    number1=['one','two','three','four','five','six','eight','nine','ten','eleven','twelve',"thirteen","fourteen","fifteen","sixteen","seventeen","eihgteen","nineteen"]
    #number2=["thirteen","fourteen","fifteen","sixteen","seventeen","eihgteen","nineteen"]
    number2=["twenty","thirty","fourty","fifty","sixty","seventy","eihgty","ninety"]
    if n>100:#１００の位が要るかどうか
        hundred_place=n//100#１００の位抽出
        ten_place=(n-hundred_place*100)//10#１０の位抽出
        one_place=n-(hundred_place*100+ten_place*10)#１の位抽出
        exnum=ten_place*10+one_place#１〜１９の場合のスケープ関数
        if (ten_place*10+one_place)<20:#１〜１９の場合のエスケープ
            print(number1[hundred_place-2],"hundred","and",number1[exnum-2],sep=" ")
        if one_place==0 and exnum>11:#１の位が0の場合
         print(number1[hundred_place-2],"hundred","and",number2[ten_place-2],sep=" ")
        else:
             print(number1[hundred_place-2],"hundred","and",number2[ten_place-3],number1[one_place-2],sep=" ")
    elif n>10 and n<100:#１０の位判定
        if n<=19：
         print(number1[n-2])
        else:
             ten_place=n//10
             one_place=n-ten_place*10
             if one_place==0 and n>11:
                print(number2[ten_place-3])
             else:
                  print(number2[ten_place-3],number1[one_place-2],sep=" ")
     elif n<10:
         print(n-2)
     else:
         print("It's not available number.")
