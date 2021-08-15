from PIL import Image
import sys
sys.path.append('../../')
import pyocr
import pyocr.builders
import logging
import config
from src.WYC2.utils import _logger_setup

"""
対象の画像をOCRする
"""

class OCR():
    def __init__(self):
        self.logger = _logger_setup(logging.DEBUG)
        self.tool = self._init_ocr_tool()

        """
        OCRの初期化
        """
    def _init_ocr_tool(self):
        tools = pyocr.get_available_tools()
        if len(tools) == 0:
            self.logger.error("No OCR tool found")
            self.logger.error("System finished")
            sys.exit(1)
        tool = tools[0]
        self.logger.debug("Will use tool '%s'" % (tool.get_name()))
        return tool

        """
        対象のファイルを読み込み、読み取った文章を返却する

        Params:
        Str: target_file
        OCR対象のファイルパス

        Returns:
        Str: text
        OCR結果の文章
        """
    def analysis(self, target_file):
        text = self.tool.image_to_string(
             Image.open(target_file),
             lang=config.LANG,
             builder=pyocr.builders.TextBuilder(tesseract_layout=6)
        )
        self.logger.debug("OCR Result: '%s'" % (text))
        return text
    
    def _trim_jpn_space(self, text):
        