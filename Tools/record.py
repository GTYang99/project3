import os
from datetime import datetime
import csv

# directory = os.path.abspath("./record")
# Python 判斷資料夾是否存在 os.path.isdir

# 建立目錄
# if not os.path.isdir(directory):
#     os.makedirs(directory)

# 建立一個空的全域變數(filename_abs)
# 建立一個新的全域變數(full_path_csvFile)，獲得絕對路徑
full_path_csvFile = None

def recordData(distance,lightValue,absolute_path):
    # 能修改全域變數的內容
    global full_path_csvFile
    print("記錄")
    current = datetime.now()
    current_date = current.date()
    filename = current_date.strftime("%Y-%m-%d.csv")
    print(filename)
    # filename_abs = f'{directory}/{filename}'
    # currentFiles = os.listdir(directory)
    
    # 相對路徑是在本目錄內的record內
    relative_path = "record/"
    # 完整的絕對路徑=絕對路徑(main.py所在位置)+相對路徑(同級的record資料夾)
    full_path_record = os.path.join(absolute_path,relative_path)

    # 如果完整的絕對路徑沒有record資料夾，則建立
    if not os.path.isdir(full_path_record):
        #建立目錄
        os.makedirs(full_path_record)

    # listdir用於返回指定的文件夾包含的文件或文件夾的名字的列表。
    currentFiles = os.listdir(full_path_record)
    full_path_csvFile = os.path.join(full_path_record,filename)
    print(full_path_csvFile)    
    
    # 建立檔案
    if filename not in currentFiles:
        print(f"沒有{filename}檔案")
        # directory是相對路徑下的record資料夾，filename是檔案名
        # csv檔案要有newline
        file = open(full_path_csvFile,'w',encoding='utf-8',newline='')
        # 表標題內容:先寫入，再確定表標題內容
        header_writer = csv.writer(file)
        header_writer.writerow(["日期","距離","光線"])
        file.close()
    with open(full_path_csvFile,"a",encoding='utf-8')as file:
        csv_writer = csv.writer(file)
        # 每次有新數據進來，就寫入row一次
        csv_writer.writerow([current.strftime("%Y-%m-%d %H:%M:%S"),distance,lightValue]) 
    
    #將資料加入至firestore
    # print("要加入的資料")
    # print('日期',current.strftime("%Y-%m-%d %H:%M:%S"))
    # print('距離',distance)
    # print("亮度",lightValue)

# 獲得數據讀取數據
def getData():
    with open(full_path_csvFile,'r',newline="")as file:
        csv_reader = csv.reader(file)
        data = list(csv_reader)
    return data