import os

directory = os.path.abspath("./record")
# Python 判斷資料夾是否存在 os.path.isdir

if not os.path.isdir(directory):
    os.makedirs(directory)

def recordData(distance,lightValue):
    print("記錄")