import tkinter as tk 
class Windows(tk.Tk):
    def __init__(self):
        super().__init__()



def main():
    window = Windows()
    window.title('數位時鐘')
    window.mainloop()

if __name__ == '__main__':
    main()