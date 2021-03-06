from PIL import Image
import sys
sys.path.append('../../')
import pyocr
import pyocr.builders
import logging
import config
from src.WYC2.utils import _logger_setup, time_func
import re

"""
対象の画像をOCRする
"""
logger = _logger_setup(logging.DEBUG)

class OCR():
    def __init__(self):
        self.tool = self._init_ocr_tool()

        """
        ocrツールの初期化
        """
    def _init_ocr_tool(self):
        tools = pyocr.get_available_tools()
        if len(tools) == 0:
            ogger.error("No OCR tool found")
            logger.error("System finished")
            sys.exit(1)
        tool = tools[0]
        logger.debug("Will use tool '%s'" % (tool.get_name()))
        return tool

        """
        対象のファイルを読み込み、読み取った文章を返却する

        Params:
        str: target_file
        OCR対象のファイルパス

        Returns:
        str: retText
        OCR結果の文章
        """

    @time_func(logger)
    def analysis(self, target_file):
        image = Image.open(target_file)
        resize_image = self._resize_img(image)
        text = self.tool.image_to_string(
             #Image.open(target_file),
             resize_image,
             lang=config.LANG,
             builder=pyocr.builders.TextBuilder(tesseract_layout=6)
        )
        logger.debug("OCR Result: '%s'" % (text))

        # 空白をトリミング
        retText = self._trim_jpn_space(text)

        return retText

        """
        日本語の間に入った空白を削除
        ocr実行時、日本語の間に空白が入る場合があり、その空白を削除する

        e.g. 今日 は testを 行 なった
        -> 今日はtest を行なった
        英字の場合、一律次の文言に空白を追加する
        それ以外の場合、空白を削除

        strの組み込み関数の場合、漢字を誤認識するとのことから、reモジュールを利用

        Params:
        str: text
        ocrの結果文章

        Returns:
        str: text
        空白をトリミングした文章
        """
    @time_func(logger)
    def _trim_jpn_space(self, text):
        r = re.compile(r'^[a-zA-Z]+$')
        words = text.split(' ')
        ret = ''
        for word in words:
            if r.match(word):
               ret = ret + word + ' '
            else:
               ret = ret + word
        return ret
    
        """
        アスペクト比を保ちながら拡大する
        
        Params:
        Image: image
        リサイズ対象画像
        
        Returns:
        Image: image.resize()
        リサイズしたImage
        """
    
    @time_func(logger)
    def _resize_img(self, image):
        width = image.size[0]
        base = int(width * 1.5)
        print(f'original {image.size[0]} x {image.size[1]}')
        resize_image = image.resize((base, int(base * image.size[1] / image.size[0])))
        print(f'resize {resize_image.size[0]} x {resize_image.size[1]}')
        return resize_image
