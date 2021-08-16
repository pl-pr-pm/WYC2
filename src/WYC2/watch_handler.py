from watchdog.observers.polling import PollingObserver as Observer
from watchdog.events import PatternMatchingEventHandler
from ocr import OCR
from clip_copy import ClipCopy
import config
"""
ディレクトリ内の変更を検知時のハンドラ

PatternMatchingEventHandler(Based on FileSystemEventHandler) を継承している

FileSystemEventHandler については以下を参照
https://pythonhosted.org/watchdog/api.html?highlight=observe#watchdog.events.FileSystemEventHandler


"""
class WatchEventHandler(PatternMatchingEventHandler):
    def __init__(self, patterns=config.TARGET_EXTENTION):
        super().__init__(patterns)
        self.ocr = OCR()

        """
        ファイル作成時のロジックを実装
        
        OCRを実行し、実行結果をclipboardにコピーする
        """
    def on_created(self, event):
        # イベントがあった画像ファイルのパスを取得
        target_file = event.src_path
        
        # OCRを実行
        text = self.ocr.analysis(target_file)
        
        # clipboardコピー実行
        ClipCopy.copy(text)