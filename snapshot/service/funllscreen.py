import pyautogui
from mss import mss


def screenshot_full(file_name):
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
    from PIL import Image
    im = Image.frombytes('RGB', sct_img.size, sct_img.bgra, 'raw', 'BGRX')
    im.save(file_name)

#screenshot_full(file_name);

