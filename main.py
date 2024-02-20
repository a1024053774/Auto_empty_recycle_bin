import winshell
import time

def empty_recycle_bin():
    try:
        winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=False)
        print("Recycle Bin emptied successfully.")
    except Exception as e:
        print(f"Error emptying Recycle Bin: {e}")

# 设置清空回收站的间隔时间（秒）
interval_seconds = 120

while True:
    empty_recycle_bin()
    # 等待指定的间隔时间
    time.sleep(interval_seconds)
