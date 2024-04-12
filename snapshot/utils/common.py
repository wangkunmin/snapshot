import time
import threading
from snapshot.service import funllscreen

def screen_task():
    while True:
        # 获取当前时间戳
        current_timestamp = time.time()
        print(current_timestamp)
        # funllscreen.screenshot_full()
        time.sleep(60)  # 暂停60秒

# 创建线程
thread = threading.Thread(target=screen_task)
thread.start()
