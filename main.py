import tkinter as tk 
from datetime import datetime
from Tools import data      #引用一個Tools外部套件(package)中的data物件

class Windows(tk.Tk):
    def __init__(self):
        super().__init__()
        # 建立物件本身的實體
        self.label = tk.Label(self,text='',font=("Times New Roman",30))
        self.label.pack(padx=50,pady=30)
        # 呼叫改變時間的function
        self.change_time()
        # 呼叫紀錄時間的function
        self.window_time()
    def change_time(self):
        # 建立一個現在時間的物件，隨時間過去，物件不停被覆蓋
        now = datetime.now()
        # 時間物件的字串格式
        now_str = now.strftime('%Y-%m-%d %H:%M:%S')     
        # 設定時間物件的標籤顯示的內容
        self.label.config(text=now_str)
        # 時間物件使用after方法，在某毫秒下，呼叫後面的變數
        self.label.after(1000,self.change_time)

    # 創建一個刪除視窗的方法
    def delete_delay(self):
        self.label.after_cancel(self.after_id)
        self.destroy
    
    def window_time(self):
        # print(f"記錄第{self.times()}秒資料")
        data.getTemperature()
        data.getLightValue()
        self.window_id = self.after(1000 * 10,self.window_time)
    
    # def times(self):
    #     now = datetime.now()
    #     mm = now.strftime('%S')   
    #     return mm
    

def main():
    window = Windows()
    window.title('數位時鐘')
    # Tkinter 支持一種稱為協議處理程序的機制。這裡，術語協議是指應用程序和窗口管理器之間的交互。最常用的協議稱為 WM_DELETE_WINDOW，用於定義當用戶使用窗口管理器顯式關閉窗口時會發生什麼。
    # 可以使用protocol方法為此進行處理程序
    window.protocol('WM_DELETE)WINDOW',window.delete_delay)
    window.mainloop()

if __name__ == '__main__':
    main()
    # data()  #引用一個Tools外部套件(package)中的data物件