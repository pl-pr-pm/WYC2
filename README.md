# WYC2

Where You Can Copy

画像でも、映像でも、どこからでも好きな言葉をコピーできるアプリケーションです。

WYC2 を利用することで、以下の課題が解決できます。

- Web などで、一瞬出た言葉を残しておきたい

.jpg, png ファイルを src/WYC2/ に配置すると画像の OCR が始まります。  
Ctrl + v で文字をペーストすることができます。

以下、デモ映像
![WYC2_resize](https://user-images.githubusercontent.com/59119963/159649252-fca2672b-ac9b-402d-913a-5420804fa2b3.gif)

### 仕組み

1. watchdog (https://pypi.org/project/watchdog/) にて、ファイル生成を監視

2. pyocr (https://pypi.org/project/pyocr/) を利用して、生成されたファイルの文字を読み取る

3. 読み取ったファイルを subprocess 経由で pbcopy 実施
