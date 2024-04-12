
from PIL.Image import Resampling
from mss import mss
from PIL import Image

from snapshot.utils import common


def screenshot_full(file_name):
    tempfile = file_name+'.temp'
    # 指定显示器的编号（例如，第一个显示器为1，第二个显示器为2，依此类推）
    display_number = 1  # 替换为您想要截图的显示器的编号
    # 使用mss模块获取指定显示器的屏幕数据
    with mss() as sct:
        # 获取指定显示器的分辨率
        monitor = sct.monitors[display_number - 1]
        # 指定截图的矩形区域（例如，左上角坐标和宽高）
        # 这里使用的是显示器的整个区域，您可以根据需要调整
        sct_img = sct.grab(monitor)

    # 使用Pillow库保存截图
    im = Image.frombuffer('RGB',sct_img.size , sct_img.bgra, 'raw', 'BGRX')
    resize_value = 2.5
    resize_size = (int(sct_img.size.width / resize_value), int(sct_img.size.height / resize_value))
    im = im.resize(size=resize_size,resample=Resampling.NEAREST)
    im.save(tempfile,'PNG', compress_level=9, quality=90)
    if common.rename_success(tempfile,file_name):
        print('')
    else:
        print('fail')


#current_timestamp = int(time.time())
#screenshot_full('/Users/edy/github/snapshot/img_cache/'+str(current_timestamp)+'.png')

