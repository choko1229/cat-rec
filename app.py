import cv2
# 保存パスの指定
save_path = "./save/"
def main():
    # カメラのキャプチャを開始
    cam = cv2.VideoCapture(0)
    # フレームの初期化
    img1 = img2 = img3 = get_image(cam)
    th = 300
    num = 1
    while True:
        # Enterキーが押されたら終了
        if cv2.waitKey(1) == 13: break
        # 差分を調べる
        diff = check_image(img1, img2, img3)
        # 差分がthの値以上なら動きがあったと判定
        cnt = cv2.countNonZero(diff)
        if cnt > th:
            print("カメラに動きを検出")
            cv2.imshow('PUSH ENTER KEY', img3)
            # 写真を画像
            cv2.imwrite(save_path + "output" + ".jpg", img3)
            num += 1
        else:
            cv2.imshow('PUSH ENTER KEY', diff)
        # 比較用の画像を保存
        img1, img2, img3 = (img2, img3, get_image(cam))
    # 後始末
    cam.release()
    cv2.destroyAllWindows()
# 画像に動きがあったか調べる関数
def check_image(img1, img2, img3):
    # グレイスケール画像に変換
    gray1 = cv2.cvtColor(img1, cv2.COLOR_RGB2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_RGB2GRAY)
    gray3 = cv2.cvtColor(img3, cv2.COLOR_RGB2GRAY)
    # 絶対差分を調べる
    diff1 = cv2.absdiff(gray1, gray2)
    diff2 = cv2.absdiff(gray2, gray3)
    # 論理積を調べる
    diff_and = cv2.bitwise_and(diff1, diff2)
    # 白黒二値化
    _, diff_wb = cv2.threshold(diff_and, 30, 255, cv2.THRESH_BINARY)
    # ノイズの除去
    diff = cv2.medianBlur(diff_wb, 5)
    return diff
# カメラから画像を取得する
def get_image(cam):
    img = cam.read()[1]
    img = cv2.resize(img, (1080, 720))
    return img
main()
