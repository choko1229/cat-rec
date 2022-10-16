import os
import shutil
import datetime
import time

#無限ループ
while True:
#出力先フォルダを選択
 os.chdir('/media/choko1229/server/Dev/cat-rec/save/')
#output.jpgを探す
 if "output.jpg" in os.listdir():
  cmo = 99
  csa = 100
  time.sleep(0.01)
#output.jpgを0.jpgとしてWeb公開ページに移動
  shutil.move("/media/choko1229/server/Dev/cat-rec/save/output.jpg", "/var/www/html/dev/cat-rec/img/0.jpg")
#Web公開フォルダを選択
  os.chdir('/var/www/html/dev/cat-rec/img/')
#処理が完了するまでループ
  while csa > 0:
#n.jpgをn+1.jpgに変更
   os.rename(str(cmo) + ".jpg",str(csa) + ".jpg")
   cmo -= 1
   csa -= 1
  print("ファイルを移動しました。")
  print(datetime.datetime.now())
 else:
  pass
