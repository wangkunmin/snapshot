import time

from snapshot.service import funllscreen
from snapshot.utils import common

img_cache_path = '/Users/edy/github/snapshot/img_cache/'


def screen_task():
    while True:
        time.sleep(1.5)  # 暂停1.5秒
        # 获取当前时间戳
        current_timestamp = int(time.time())
        funllscreen.screenshot_full(img_cache_path + str(current_timestamp) + '.png')

def upload_task():
    while True:
        time.sleep(3)  # 暂停3秒
        print('上传')


screen_task_thread = common.creat_task(screen_task)
screen_task_thread.start()

upload_task_thread = common.creat_task(upload_task)
upload_task_thread.start()
