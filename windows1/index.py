import tkinter as tk
from tkinter import Button,Frame
from tools import Taiwan_AQI

class Window(tk.Tk):

    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        try:
            self.aqi_list = Taiwan_AQI.download_aqi()
        except Exception as err:
            print(str(err))
            return
        
        Button(self,text='"目前空氣aqi品質最好的3個"', font=('Helvetica', '24'),pady=10,command=self.btn5_click).pack(fill=tk.X)
        '''
        Button(self,text='按鈕1',command=self.btn1_click).pack()
        Button(self,text='按鈕2', padx=10, pady=20,command=self.btn2_click).pack()
        
        Button(self,text='按鈕3', padx=10, pady=20,font=('Helvetica', '24'), command=self.btn3_click).pack()
        
        Button(self,text='按鈕4', font=('Helvetica', '24'),pady=10,command=self.btn4_click).pack(fill=tk.X)
        '''

        bottom_frame = Frame(self, bg='#ffffff')
        btn5 = Button(bottom_frame, text='按鈕5', font=('Helvetica', '24'))
        btn5.bind('<Button-1>',self.other_btn_click)
        btn5.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        btn6 = Button(bottom_frame, text='按鈕6', font=('Helvetica', '24'),pady=10)
        btn6.bind('<Button-1>',self.other_btn_click)
        btn6.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        btn7 = Button(bottom_frame, text='按鈕7', font=('Helvetica', '24'),pady=10)
        btn7.bind('<Button-1>',self.other_btn_click)
        btn7.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        bottom_frame.pack(expand=True,fill=tk.BOTH)

    def get_best(dataList) -> list:
        sorted_data = sorted(dataList, key=lambda a:a.aqi, reverse=True)
        def out_aqi_999(site):
            return site.aqi != 999
        filter_data = filter(out_aqi_999, sorted_data)
        filter_data = list(filter_data)
        return filter_data[-3:]


    def btn5_click(self):
        good3_list = self.get_best(self.aqi_list)
        print("目前空氣aqi品質最好的3個")
        good3_list.reverse()
        for site in good3_list:
            print(site)

'''
    def btn1_click(self):
        print("按鈕1按下")
    
    def btn2_click(self):
        print("按鈕2按下")    
    
    def btn3_click(self):
        print("按鈕3按下")
    
    def btn4_click(self):
        print("按鈕4按下")
'''
    def other_btn_click(self, event):
        if event.widget['text'] == '按鈕5':
            print("按鈕5按下")
        elif event.widget['text'] == '按鈕6':
            print("按鈕6按下")
        elif event.widget['text'] == '按鈕7':
            print("按鈕7按下")
            


'''
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        Button(self,text="按鈕1",font=('Helvetica', '24'),pady=10,command=self.btn1_click).pack(fill=tk.X)
        Button(self,text="按鈕2",font=('Helvetica', '24'),pady=10,command=self.btn2_click).pack(fill=tk.X)

        bottom_frame  = Frame(self,bg="#ffffff")
        Button(bottom_frame,text="按鈕3",font=('Helvetica', '24')).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        Button(bottom_frame,text="按鈕4",font=('Helvetica', '24')).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        Button(bottom_frame,text="按鈕5",font=('Helvetica', '24')).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        bottom_frame.pack(expand=True,fill=tk.BOTH)

    def btn1_click(self):
        print("按鈕1按下")

    def btn2_click(self):
        print("按鈕2按下")
        '''

def main():
    window = Window()
    window.title("這是第一個視窗")
    window.geometry('400x300')
    window.mainloop()

if __name__ == "__main__":
    main()