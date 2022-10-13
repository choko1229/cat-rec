import os
import shutil
import datetime
import time
while True:
 os.chdir('画像出力フォルダパス')
 if "output.jpg" in os.listdir():
  cmo = 99
  csa = 100
  time.sleep(0.01)
  shutil.move("出力画像パス", "Webサーバー画像フォルダ")
  os.chdir('Webサーバー画像フォルダ')
  while csa > 0:
   os.rename(str(cmo) + ".jpg",str(csa) + ".jpg")
   cmo -= 1
   csa -= 1
  print("ファイルを移動しました。")
  print(datetime.datetime.now())
 else:
  pass
