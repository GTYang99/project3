import tkinter as tk 
from datetime import datetime

class Windows(tk.Tk):
    def __init__(self):
        super().__init__()
        # 建立物件本身的實體
        self.label = tk.Label(self,text='',font=("Times New Roman",30))
        self.label.pack(padx=50,pady=30)
        # 呼叫改變時間的function
        self.change_time()
    def change_time(self):
        # 建立一個現在時間的物件，隨時間過去，物件不停被覆蓋
        now = datetime.now()
        # 時間物件的字串格式
        now_str = now.strftime('%Y-%m-%d %H:%M:%S')     
        # 設定時間物件的標籤顯示的內容
        self.label.config(text=now_str)
        # 時間物件使用after方法，在某毫秒下，呼叫後面的變數
        self.label.after(1000,self.change_time)

    def delete_delay(self):
        self.label.after_cancel(self.after_id)
        self.destroy

    

def main():
    window = Windows()
    window.title('數位時鐘')
    window.protocol('WM_DELETE)WINDOW',window.delete_delay)
    window.mainloop()

if __name__ == '__main__':
    main()