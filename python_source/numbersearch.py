i=10
while True:
  n=int(input("答えは？"))
  if n==i:
      print("当たりです。")
      break
  elif n>i:
      print("もっと小さいです。")
      continue
  elif n<i:
      print("もっと大きいです。")
      continue
