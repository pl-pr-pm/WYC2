from watchdog.observers.polling import PollingObserver as Observer
from watchdog.events import PatternMatchingEventHandler
import time
from watch_handler import WatchEventHandler

def main():
    wdir = '.'
    evh = WatchEventHandler()
    obs = Observer()
    obs.schedule(evh, wdir)
    obs.start()

    try:
        while True:
            time.sleep(0.01)
    except KeyboardInterrupt:
        obs.stop()
    finally:
        obs.join()

if __name__ == '__main__':
    main()