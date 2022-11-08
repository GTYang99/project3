import os
from datetime import datetime

directory = os.path.abspath("./record")
# Python 判斷資料夾是否存在 os.path.isdir

# 建立目錄
if not os.path.isdir(directory):
    os.makedirs(directory)

def recordData(distance,lightValue):
    print("記錄")
    current = datetime.now()
    current_date = current.date()
    filename = current_date.strftime("%Y-%m-%d.csv")
    print(filename)
    filename_abs = f'{directory}/{filename}'
    currentFiles = os.listdir(directory)
    # 建立檔案
    if filename not in currentFiles:
        print(f"沒有{filename}檔案")
        # directory是相對路徑下的record資料夾，filename是檔案名
        file = open(filename_abs,'w',encoding='utf-8')
        file.close()