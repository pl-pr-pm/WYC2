import tkinter as tk
# 本来はKivyを使いたかったが、
# OSX ではタイムアウトを利用していなかったこと
# ポップアップ表示で 謎のエラーが発生し、利用できなかったため、python標準のtk-interを利用する

"""
plyer/platforms/macosx/notification.py", line 38, in _notify
usrnotifctr.setDelegate_(self)
AttributeError: 'NoneType' object has no attribute 'setDelegate_'
"""

"""
OCRコピー完了のメッセージを表示する

TODO:
windowにLabelを表示させる
202108現在、watch_dogからの呼び出しでは、Labelが表示されない
別ファイルからのインポート、実行に問題がないことは確認済み
おそらく、 watch_dog のスレッド関係ではないかと考えている
"""

class Message():

    def __init__(self):
        pass

    def _set_up(self, root):
        root.geometry("300x50")
        # ウインドウを最前面に配置
        root.attributes("-topmost", True)
    
    def _screen(self, root):
        root.title('WYC2')
        root.after(5000, lambda: root.destroy())

    def execution(self):
        root = tk.Tk()
        self._set_up(root)
        self._screen(root)
        root.mainloop()