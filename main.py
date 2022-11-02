import tkinter as tk 
from datetime import datetime
from pyglet import font

class Windows(tk.Tk):
    def __init__(self):
        super().__init__()
        now = datetime.now()
        now_str = now.strftime('%Y-%m-%d %H:%M:%S')
        font.add_file('action_man.ttf')
        
        tk.Label(self,text=now_str,font=("Times New Roman",30)).pack(padx=50,pady=30)


def main():
    window = Windows()
    window.title('數位時鐘')
    window.mainloop()

if __name__ == '__main__':
    main()