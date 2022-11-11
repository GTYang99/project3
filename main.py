import tkinter as tk 
from datetime import datetime
from Tools import data,record   #外部一個Tools外部套件(package)中的data與record物件
from tkinter import ttk
import os


class Windows(tk.Tk):
    def __init__(self):
        super().__init__()
        # 建立物件本身的實體
        self.label = tk.Label(self,text='',font=("Times New Roman",30))
        self.label.pack(padx=50,pady=30)
        # 建立自己的實體，呼叫CustomView        self.customView = CustomView(self)
        # =========建立查看實時數據的視窗實體=========
        # Treeview基本參數
        # columns	欄位的字串，可以設定欄位數。
        self.customView = CustomView(self,columns=('#1','#2','#3'),show='headings')
        # 微調scroll bar的位置
        self.customView.pack(side=tk.LEFT,padx=(20,0),pady=(0,20))
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

        # data.getTemperature()
        # data.getLightValue()
        # data.getDistance()
        # self.window_id = self.after(1000 * 3,self.window_time)

        # 修改為:按照時間記錄距離，當大於100cm時，紀錄的距離為100
        distance = data.getDistance()
        print(distance)
    
        if distance < 100: 
            print(f"距離:{distance:.2f}公分")
        else:
            print(f"距離:大於100公分")
            distance = 1
        lightValue = data.getLightValue()
        print(f"光線:{lightValue:.1f}")
        
        #取得檔案絕對位置
        absolute_path = os.path.dirname(__file__)

        #記錄資料
        # record.recordData(distance=100,lightValue=200)
        record.recordData(distance=distance,lightValue=lightValue,absolute_path=absolute_path)

        #取得資料
        #建立實體(all_data)，呼叫record的module中的getData方法
        all_data = record.getData()
        # print(all_data)
        self.customView.addData(all_data)

        self.window_id = self.after(1000 * 3,self.window_time)
    
    # def times(self):
    #     now = datetime.now()
    #     mm = now.strftime('%S')   
    #     return mm

# 新增一個物件，作為顯示實時數據的視窗內容
class CustomView(ttk.Treeview):
    def __init__(self,master,**kwargs):
        super().__init__(master,**kwargs)
        # Treeview基本參數
        # .heading ("欄位",text="內容")
        self.heading('#1',text="日期")
        self.heading('#2',text="距離")
        self.heading('#3',text="光線")
                
        #==========建立scrollbar==========
        scrollbar = ttk.Scrollbar(master,orient=tk.VERTICAL,command=self.yview)
        self.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT,fill=tk.BOTH,padx=(0,20))

    def addData(self,data):
        #清除第一筆資料
        data.pop(0)
        #反向
        data.reverse()        
        # 清除所有資料
        for i in self.get_children():
            self.delete(i)
        #新增所有資料
        for item in  data:
            self.insert('',tk.END,values=item)    




def main():
    window = Windows()
    window.title('光線和距離監測器')
    # Tkinter 支持一種稱為協議處理程序的機制。這裡，術語協議是指應用程序和窗口管理器之間的交互。最常用的協議稱為 WM_DELETE_WINDOW，用於定義當用戶使用窗口管理器顯式關閉窗口時會發生什麼。
    # 可以使用protocol方法為此進行處理程序
    window.protocol('WM_DELETE)WINDOW',window.delete_delay)
    window.mainloop()

if __name__ == '__main__':
    main()
    # data()  #引用一個Tools外部套件(package)中的data物件