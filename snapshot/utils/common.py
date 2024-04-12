import threading
import os


def creat_task(task) -> threading.Thread:
    # 创建线程
    return threading.Thread(target=task)


def rename_success(current_filename, new_filename) -> bool:
    # 检查文件是否存在
    if os.path.exists(current_filename):
        try:
            # 尝试重命名文件
            os.rename(current_filename, new_filename)
            return True
        except OSError as e:
            # 如果发生错误，打印错误信息
            print(f"Error renaming file: {e}")
            return False
    else:
        print(f"File {current_filename} does not exist.")


def remove_file(filename):
    # 检查文件是否存在
    if os.path.exists(filename):
        try:
            os.remove(filename)
        except OSError as e:
            print(f"Error deleting file: {e}")
    else:
        print(f"File {filename} does not exist.")
