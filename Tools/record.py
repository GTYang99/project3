import os
from datetime import datetime
import csv

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
        # csv檔案要有newline
        file = open(filename_abs,'w',encoding='utf-8',newline='')
        # 表標題內容:先寫入，再確定表標題內容
        header_writer = csv.writer(file)
        header_writer.writerow(["日期","距離","光線"])
        file.close()
    with open(filename_abs,"a",encoding='utf-8')as file:
        csv_writer = csv.writer(file)
        # 每次有新數據進來，就寫入row一次
        csv_writer.writerow([current.strftime("%Y-%m-%d %H:%M:%S"),distance,lightValue]) 